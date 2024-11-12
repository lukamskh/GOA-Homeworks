class Book {
    constructor(title, author = "Unknown") {
        this.title = title;
        this.author = author;
    }

    getDetails() {
        console.log("Title: " + this.title + ", Author: " + this.author);
    }
}


class Classroom {
    constructor(students) {
        this.students = students;
    }

    countStudents() {
        console.log("Number of students: " + this.students.length);
    }
}


class Counter {
    constructor() {
        this.value = 0;
    }

    increment() {
        this.value += 1;
    }

    getValue() {
        return this.value;
    }
}


class Light {
    constructor() {
        this.state = "off";
    }

    toggle() {
        this.state = this.state === "off" ? "on" : "off";
    }
}


class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }

    getDetails() {
        console.log("Product: " + this.name + ", Price: " + this.price + " USD");
    }
}


class User {
    constructor(username, contact) {
        this.username = username;
        this.contact = contact;
    }

    getContactInfo() {
        console.log("Username: " + this.username + ", Email: " + this.contact.email + ", Phone: " + this.contact.phone);
    }
}


class Library {
    constructor(books) {
        this.books = books;
    }

    listBooks() {
        this.books.forEach(function(book) {
            console.log("Title: " + book.title + ", Author: " + book.author);
        });
    }
}


class Cart {
    constructor() {
        this.items = [];
    }

    addItem(item) {
        this.items.push(item);
    }

    getItems() {
        console.log("Items in cart: " + this.items.join(', '));
    }
}


class Student {
    constructor(name, marks) {
        this.name = name;
        this.marks = marks;
    }

    hasPassed() {
        const average = this.marks.reduce(function(sum, mark) {
            return sum + mark;
        }, 0) / this.marks.length;
        return average >= 50;
    }
}