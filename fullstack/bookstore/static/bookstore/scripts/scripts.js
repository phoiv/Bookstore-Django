function Book(title, url, price, quantity) {
    this.title = title;
    this.imgURL = url;
    this.price = price;
    this.quantity = quantity;
}


// console.log("loaded")
// let cartContent = loadCart();

// console.log(cartContent);




const html = document.querySelector("html");
const cartTgl = document.querySelector(".cart-icon")
const myCartOvr = document.querySelector("#my-cart-overlay")
const myCart = document.querySelector("#my-cart")
const burger = document.querySelector(".toggler");
const menu = document.querySelector("#nav-menu");
// const addToBskt = document.querySelectorAll(".price-buy button");
const contentOvr = document.querySelector(".content-overlay");
const cartCount = document.querySelector(".cart-count span:first-child");

const cart_buttons = document.querySelectorAll("#my-cart button");

let isNavOpen = false;
let isCartOpen = false;



// updateCartCount();

// myCart.innerHTML += tt;
// myCart.innerHTML += tt;
// myCart.innerHTML += tt;
// myCart.innerHTML += tt;


/*---------------------------------
-----------EVENT LISTENERS---------
---------------------------------*/

// cart_buttons.forEach((button) => {
//     console.log("hi")
//     button.addEventListener('click', function () {
//         console.log("clicked ", button.name, "for book ", button.value)
//         updateCart(button.name, button.value)
//     })
// })

function updateCart(action, book_pk) {
    console.log(action, " book ", book_pk)
    let url = '/update_cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
        body: JSON.stringify({ 'action': action, 'book_pk': book_pk })
    }).then(response => {
        return response.json()
    }).then(count => {
        console.log(count)
        $("#my-cart-overlay").load("/cart/");
        $(".cart-count span:first-child").text(count)

    })

}


//make sure nav fade in works correctly after resizing
window.addEventListener('resize', function () {
    if (window.innerWidth > 950) {
        menu.className = "";
        isNavOpen = false;
        if (isCartOpen) {
            contentOvr.style.display = "block";
        }
        if (!isCartOpen)
            html.style.overflow = "initial"
    }
    else if (!isNavOpen) {
        menu.className = "close"
        isNavOpen = false;
    }
})

burger.addEventListener("click", function () {
    console.log(isNavOpen)
    //if its open close it
    if (isNavOpen) {
        html.style.overflow = "initial"
        menu.classList.add("close")
        menu.classList.remove("open")
        isNavOpen = !isNavOpen
    }
    //if its close open it
    else {
        html.style.overflow = "hidden"
        menu.classList.add("open")
        menu.classList.remove("close")
        isNavOpen = !isNavOpen
        //if cart is open close it
        if (isCartOpen) {
            contentOvr.style.display = "none";
            myCartOvr.classList.toggle("open")
            isCartOpen = !isCartOpen;
        }
    }
})

contentOvr.addEventListener("click", function () {
    console.log("here")
    if (isCartOpen) {
        myCartOvr.classList.toggle("open")
        html.style.overflow = "initial"
        contentOvr.style.display = "none";
        isCartOpen = !isCartOpen;
    }
})


cartTgl.addEventListener("click", function () {
    console.log(isCartOpen)
    //if its close open it
    if (!isCartOpen) {
        // generateMyCart();
        myCartOvr.classList.toggle("open")
        html.style.overflow = "hidden"
        contentOvr.style.display = "block";
        isCartOpen = !isCartOpen;
        //if nav is open close it
        if (isNavOpen) {
            contentOvr.style.display = "none";
            menu.classList.add("close")
            menu.classList.remove("open")
            isNavOpen = !isNavOpen
        }
    }
    else {
        myCartOvr.classList.toggle("open")
        html.style.overflow = "initial"
        contentOvr.style.display = "none";
        isCartOpen = !isCartOpen;
    }
})

//add to basket function
// addToBskt.forEach((button) => {
//     button.addEventListener("click", function () {
//         console.log(this.value);
//         cartContent[this.value - 1].quantity++;
//         //update the save
//         localStorage.setItem("cartContent", JSON.stringify(cartContent))
//         updateCartCount();
//         const tooltip = document.createElement("div")
//         tooltip.innerText = "+1"
//         tooltip.classList.add("book-added-tooltip")
//         this.appendChild(tooltip)
//         setTimeout(function () {
//             tooltip.remove()
//         },
//             2000)
//     })
// })



/*---------------------------------
-----------OTHER FUNCTIONS---------
---------------------------------*/


// function loadCart() {
//     let cartContentTemp = [];
//     //if theres no cart content in memory initialise it
//     if (localStorage.getItem("cartContent") == null) {
//         let newBook = new Book("A Game Of Thrones", "images/got.jpg", '11.70', 0);
//         cartContentTemp.push(newBook);
//         newBook = new Book("Dune", "images/dune.jpg", '9.80', 0);
//         cartContentTemp.push(newBook);
//         newBook = new Book("The Hobbit, or There and Back Again", "images/hobbit.jpg", '8.90', 0);
//         cartContentTemp.push(newBook);
//         newBook = new Book("Foundation", "images/found.jpg", '12', 0);
//         cartContentTemp.push(newBook);
//         localStorage.setItem("cartContent", JSON.stringify(cartContentTemp))
//         return cartContentTemp;
//     }
//     return JSON.parse(localStorage.getItem("cartContent"));
// }

// function generateMyCart() {
//     let sum = 0;
//     myCart.innerHTML = "";
//     cartContent.forEach((book, index) => {
//         if (book.quantity > 0) {
//             let newBookOnCart = document.createElement("div");
//             newBookOnCart.classList.add("book-item-cart")
//             newBookOnCart.id = `book${index + 1}`
//             newBookOnCart.innerHTML = `<div class="book-cover-cart"><img src=${book.imgURL} alt=""></div>
//                                        <div class="book-item-body-cart">
//                                             <p class="book-title-cart">${book.title}</p>
//                                             <div class="book-info"><span>QUANTITY: ${book.quantity}</span>
//                                             <div class="quan-buttons">
//                                                 <button class="inc-button">+</button>
//                                                 <button class="dec-button">-</button>                        
//                                             </div>
//                                             <button class="delete-button">X</button>
//                                             <span>${book.price}€</span></div>
//                                        </div>`
//             myCart.appendChild(newBookOnCart);
//             sum += eval(book.quantity * book.price);
//             //we give the buttons a value which ties it with a book on our cartContent array
//             newBookOnCart.querySelector(".book-info .delete-button").value = index + 1;
//             newBookOnCart.querySelector(".book-info .inc-button").value = index + 1;
//             newBookOnCart.querySelector(".book-info .dec-button").value = index + 1;
//             //...and add event listener to the buttons
//             newBookOnCart.querySelector(".book-info .delete-button").addEventListener("click", deleteFromCart)
//             newBookOnCart.querySelector(".book-info .inc-button").addEventListener("click", increaseQuan)
//             newBookOnCart.querySelector(".book-info .dec-button").addEventListener("click", decreaseQuan)
//         }
//     })
//     const priceBox = document.querySelector(".price-total");
//     priceBox.innerText = "Total: " + sum.toFixed(2) + "€";
//     //take care of empty cart
//     if (sum == 0) {
//         let pEmpty = document.createElement("p")
//         pEmpty.innerText = "There is nothing here"
//         myCart.appendChild(pEmpty)
//     }

// }


// function updateCart(book, newQuan) {
//     console.log(`book${book + 1}`, newQuan)
//     cartContent[book].quantity = newQuan;
//     const bookOnCart = document.querySelector(`#book${book + 1}`)
//     console.log(bookOnCart)
//     const quanField = bookOnCart.querySelector(".book-info span:first-child").innerText = `QUANTITY: ${newQuan}`
//     updateTotalPrice()
//     updateCartCount()
// }

// function updateTotalPrice() {

//     let sum = 0;
//     cartContent.forEach((book) => {
//         sum += book.quantity * book.price;
//     })
//     console.log(sum)
//     const priceBox = document.querySelector(".price-total");
//     priceBox.innerText = "Total: " + sum.toFixed(2) + "€";
//     if (sum == 0) {
//         let pEmpty = document.createElement("p")
//         pEmpty.innerText = "There is nothing here"
//         myCart.appendChild(pEmpty)
//         return;
//     }

// }

// function updateCartCount() {
//     let sum = 0;
//     cartContent.forEach(book => {
//         sum += book.quantity;
//     })
//     // console.log(sum)
//     if (sum == 0) cartCount.innerHTML = "";
//     else
//         cartCount.innerHTML = sum;
// }


// function increaseQuan() {
//     console.log("increasing quan")
//     let quan = cartContent[this.value - 1].quantity;
//     updateCart(this.value - 1, ++quan)
//     localStorage.setItem("cartContent", JSON.stringify(cartContent))
// }

// function decreaseQuan() {
//     console.log("decreasing quan")
//     let quan = cartContent[this.value - 1].quantity;
//     if (quan > 1)
//         updateCart(this.value - 1, --quan)
//     localStorage.setItem("cartContent", JSON.stringify(cartContent))
// }

// function deleteFromCart() {
//     console.log(`deleting book${this.value}`)
//     updateCart(this.value - 1, 0)
//     document.querySelector(`#book${this.value}`).remove()
//     localStorage.setItem("cartContent", JSON.stringify(cartContent))
//     // console.log("deleted book", this.value)
//     // this.parentNode.parentNode.parentNode.remove();
//     // //update price
//     // const priceBox = document.querySelector(".price-total");
//     // const oldPrice = priceBox.innerText.match(/(\d)+(\.)?(\d)*/g)[0];
//     // const newPrice = oldPrice - cartContent[this.value - 1].quantity * cartContent[this.value - 1].price;
//     // priceBox.innerText = "Total: " + newPrice.toFixed(2) + "€";
//     // if (newPrice == 0) {
//     //     let pEmpty = document.createElement("p")
//     //     pEmpty.innerText = "There is nothing here"
//     //     myCart.appendChild(pEmpty)
//     // }
//     // //update cart quantities on temp and memory
//     // cartContent[this.value - 1].quantity = 0;
//     // localStorage.setItem("cartContent", JSON.stringify(cartContent))
//     // updateCartCount();
// }

