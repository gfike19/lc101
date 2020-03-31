// Define your Book class here:
class Book {
  constructor(title, author, copyright, ISBN, pages, checked, discarded){
    this.title = title;
    this.author = author;
    this.copyright = copyright;
    this.ISBN = ISBN;
    this.pages = pages;
    this.checked = checked;
    this.discarded = discarded;
  }
}

// Define your Manual and Novel classes here:
class Manual extends Book {
  constructor(){
    super();
  }
}

class Novel extends Book {
  constructor(){
    super();
    this.title = 'Pride and Prejudice';
    this.author = 'Jane Austen';
  }
}

// Declare the objects for part 2 here:
// let myNovel = new Novel(, , 1813, 1111111111111, 432, 32, 'No');
let test = new Novel();
console.log(test)

// Code part 3 here:
