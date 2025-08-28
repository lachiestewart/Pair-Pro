from tree_sitter_typescript import language_typescript
from config import EMBEDDING_URL, EMBEDDING_MODEL, QDRANT_URL, MY_COLLECTION
from qdrant import Qdrant
from embedder import Embedder


# from tree_sitter import Language, Parser
from tree_sitter_typescript import language_typescript
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, Node

WANTED_NODES = [
    "function_declaration",
    "class_declaration",
    "interface_declaration",
    "enum_declaration",
    "method_definition",
]

MAX_SEGMENT_LENGTH = 40


LANGUAGE_COMMENT = {"ts": "//"}


def find_wanted_node(node: Node) -> Node | None:
    if node.type in WANTED_NODES:
        return node
    for child in node.children:
        result = find_wanted_node(child)
        if result:
            return result
    return None


def summarise_node(node: Node, code_bytes: bytes) -> str:
    current = find_wanted_node(node)
    if not current:
        return ""
    start = current.start_byte
    end = current.end_byte
    code_segment = code_bytes[start:end].decode("utf-8")
    first_line = code_segment.strip().splitlines()[0]
    return f"{current.type}: {first_line}"


def collect_nodes(node: Node, code_bytes: bytes, parent_comments=None):
    if parent_comments is None:
        parent_comments = []

    nodes = []
    node_summaries = []

    if node.type in WANTED_NODES:
        if node.end_point.row - node.start_point.row <= MAX_SEGMENT_LENGTH:
            return [(node, parent_comments.copy())]

        # Get summaries of direct children
        child_summaries = []
        for child in node.children:
            if child.type in WANTED_NODES:
                child_summaries.append((child, summarise_node(child, code_bytes)))
        print("children summaries for " + summarise_node(node, code_bytes))
        print(child_summaries)

        # Replace each child's code segment in this node's code with its summary
        code_segment = code_bytes[node.start_byte : node.end_byte].decode("utf-8")
        offset = node.start_byte
        segments = []
        last_idx = 0

        for child, summary in sorted(child_summaries, key=lambda x: x[0].start_byte):
            rel_start = child.start_byte - offset
            rel_end = child.end_byte - offset
            segments.append(code_segment[last_idx:rel_start])
            segments.append(f"/* {summary} */")
            last_idx = rel_end

        segments.append(code_segment[last_idx:])
        summarised_code = "".join(segments)
        node_summaries.append(f"{node.type}: {summarised_code.strip().splitlines()[0]}")
        node_summaries.append(summarise_node(node, code_bytes))

    for child in node.children:
        nodes.extend(collect_nodes(child, code_bytes, parent_comments + node_summaries))
    return nodes


def main():
    language = Language(language_typescript())
    parser = Parser(language)

    with open("repo/test.ts", "r") as file:
        code = file.read()

    code_bytes = bytes(code, "utf8")

    tree = parser.parse(code_bytes)

    nodes = collect_nodes(tree.root_node, code_bytes)

    with open("output.ts", "w", encoding="utf-8") as out_file:
        for node, parent_comments in nodes:
            context = " > ".join(p for p in parent_comments)
            out_file.write(
                f"{LANGUAGE_COMMENT['ts']} {context + '->' if context else ''} {node.type}: \n{code_bytes[node.start_byte:node.end_byte].decode('utf-8')}\n\n"
            )


if __name__ == "__main__":
    main()
    # embedder = Embedder(url=EMBEDDING_URL, model=EMBEDDING_MODEL)

    # name = "<name>"
    # content = "<contents>"

    # embedded_point = embedder.embed_payload({"name": name, "content": content})

    # print(embedded_point)

    # qdrant_client = Qdrant(url=QDRANT_URL)
    # # qdrant_client.create_collection(MY_COLLECTION["NAME"], MY_COLLECTION["CONFIG"])
    # qdrant_client.store_embedded_point(MY_COLLECTION["NAME"], embedded_point)

    # print("Done")
