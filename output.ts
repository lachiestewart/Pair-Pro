//  class_declaration: 
class Greeter {
    constructor(private name: string) { }

    greet(): string {
        return `Hello, ${this.name}!`;
    }
}

//  function_declaration: 
function greet(name: string): string {

    function getGreeting(): string {
        return `Hello, ${name}!`;
    }

    return getGreeting();
}

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
constructor(private id: number) { }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
increment(): void {
        this.counter++;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
decrement(): void {
        this.counter--;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
reset(): void {
        this.counter = 0;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
addData(item: string): void {
        this.data.push(item);
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
removeData(item: string): boolean {
        const index = this.data.indexOf(item);
        if (index !== -1) {
            this.data.splice(index, 1);
            return true;
        }
        return false;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
getData(): string[] {
        return [...this.data];
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
getCounter(): number {
        return this.counter;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
randomizeCounter(): void {
        this.counter = Math.floor(Math.random() * 100);
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
findData(query: string): string | undefined {
        return this.data.find(item => item.includes(query));
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
clearData(): void {
        this.data = [];
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
isEmpty(): boolean {
        return this.data.length === 0;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
getId(): number {
        return this.id;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
toString(): string {
        return `BigRandomClass(id=${this.id}, counter=${this.counter}, data=[${this.data.join(", ")}])`;
    }

// class_declaration: /*  */ /*  */ /* method_definition: constructor(private id: number) { } */ > class_declaration: class BigRandomClass {-> method_definition: 
static generateRandomInstance(): BigRandomClass {
        const instance = new BigRandomClass(Math.floor(Math.random() * 1000));
        for (let i = 0; i < 5; i++) {
            instance.addData(`item${Math.floor(Math.random() * 100)}`);
        }
        instance.randomizeCounter();
        return instance;
    }

//  function_declaration: 
function greet2(name: string): string {
    return `Hello, ${name}!`;
}

