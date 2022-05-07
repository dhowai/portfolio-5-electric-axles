<h1 align="left">Electric Axles</h1>

<img src="docs/readme/">

This project was focused on creating a Full Stack developed fictional e-commerce store using the Django Framework, Python, HTML, CSS, and Javascript.
The project also uses stripe for online test payments and Heroku Postgres as a relational database.

Electric Axles is an e-commerce store that primarily sells a variety of personal electric vehicles. This project is for educational purposes only, images used are of existing items being sold in the current market.

The live link can be found here: https://portfolio-5-electric-axles.herokuapp.com/

***

#   Table of Contents:
* [User Experience](#user-experience)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Design](#design)
        * [1. Typography](#typography)
        * [2. Color Scheme](#color-scheme)
        * [3. Imagery](#imagery)
* [Database Schema](#database-schema)
* [Technologies Used](#technologies-used)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)
* [Marketing](#marketing)
* [Testing](#testing)
    * [User Stories Testing](#user-stories-testing)
    * [Code Validation](#code-validation)
    * [Maual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowlegments](#credits)

***

#  User Experience:

Github projects was used to organize the project's user stories. Each user story was categorized and labeled according to relevance/importance and was placed in a milestone. 
All these user stories were placed on a basic kanban board and organized by: to do, in progress, and done.
User stores were placed accordingly when been worked on and on completion were moved to done and had their issue closed. This was reflected in the milestones giving a better visual representation of progress.
Link to [Milestones](https://github.com/dhowai/portfolio-5-electric-axles/milestones) and [Projects](https://github.com/dhowai/portfolio-5-electric-axles/projects/1).

-   ## User Stories:

    -   ### First Time visitor/User Goals
        -   As a first time User, I want to be able to easily navigate the site.
        -   As a first time User, I want to have the ability to register on the site.
        -   As a first time User, I want to view the complete store content.
        -   As a first time User, I want to be able to purchase items.

    -   ### Returning registered User Goals 
        -   As a registered User, I want to have the ability to log in to the site with my credentials.
        -   As a registered User, I want to be able to purchase items.
        -   As a registered User, I want to be able to save items for later purchase.
        -   As a registered User, I want to be able to edit/save any information I entered Prior.
        -   As a registered User, I want to have the ability to log out of the site. 

    -   ### Frequent User Goals 
        -   As a frequent User, I want to easily find any new updates to the site.
        -   As a frequent User, I want to easily purchase an item with previous information saved.
    
    -   ### Administrator User Goals
        -   As an Administrator, I want to be able to access the Administration panel.
        -   As an Administrator, I want to have the ability to manage site products.
        -   As an Administrator, I want to be able to give other users administrator abilities to help maintain the site.
[Back to Top](#table-of-contents)

-   ## Wireframes

    Balsamiq was used to create initial site layout wireframes to get a rough idea of what the site should look like.

    -   ### [Home Page](docs/wireframe/home.png) - A welcome page for the site with brief details.
    -   ### [Register Page](docs/wireframe/register.png) - A page for user to register an account.
    -   ### [Sign Page](docs/wireframe/sign-in.png) - A page for users to sign-in, similar for log-out
    -   ### [Products](docs/wireframe/products.png) - A page for all products being sold
    -   ### [Product Details](docs/wireframe/product-details.png) - A page for a single product with more details.
    -   ### [Product Management](docs/wireframe/product-management.png) - A page to edit/add products to site.
    -   ### [Basket](docs/wireframe/basket.png) - A page to view all products in users basket.
    -   ### [Checkout](docs/wireframe/checkout.png) - A page for the user to checkout items in basket.
    -   ### [Profile](docs/wireframe/profile.png) - A page for the user to update any information enter prior.
    -   ### [Mobile Home](docs/wireframe/mobile-home.png) - Mobile view for home page
    -   ### [Mobile Products](docs/wireframe/mobile-products.png) - Mobile view for all products page
    -   ### [Mobile Products Details](docs/wireframe/mobile-products-detail.png) - Mobile view for a single products page
    -   ### [Mobile Basket](docs/wireframe/mobile-basket.png) - Mobile view for users basket, similar for checkout page.

   
[Back to Top](#table-of-contents)

-   ## Design

    -   ### Typography
        -   The Roboto font was used for the headings, the Lato font is used for the body elements and both have sans-serif as a backup. These fonts were chosen because they complement each other well.

    -   ### Color Scheme
        -  Update the color scheme to pallet

        <img src="docs/readme/pallet.png">
        
    -   ### Imagery 
        -   The images used for the products were taken from a real business called [Ride And Glide](https://www.rideandglide.co.uk/), images were only used for educational purposes and all rights of these images belong to the site.

[Back to Top](#table-of-contents)

# Database Schema

SQLite was used during the development of the site and then moved to Postgres in Heroku.

 <img src="docs/schema/database-schema.png">


-   ##  Applications

    -   ### Product
        - This app controls the products in the store. There are three models used to store various data: `Category`, `Product` and `ProductReview`.
        
        - `Products` enables items to be added to the database for them to be viewed and purchased. Only users that have superuser status can add items to the store through the `add_product` view. This model is connected to the `Category` model through a foreign key.
        - `Category` stores category names and is connected to the `products` model, which allows the products to be filtered easily on the site.
        - `ProductReview` allows the user to create a review for a product. It is connected by the product slug. It is also connected to the user's username which gets displayed on successful reviews posted.
    
    -   ### Checkout  
        - This app handles the purchasing of items in the store. It contains two models: `Order` and `OrderLineItem`.

        - `Order` contains the user's shipping details needed for the order to be completed. It is a foreign key to the `UserProfile` which stores the user's information is saved. It also contains the items in the basket, the total costs, and stripe_pid    which is used to handle the online card payments. Also generates a unique order_number through UUID.
        - `OrderLineItem` stores all details for the specific order. It has a foreign key to `Product` and `Order` to capture all this information.

    -   ### Profiles
        - This app contains a model `UserProfile` which stores the user's default billing information. It is also connected to the User model through a OneToOneField.

    -   ### Wishlist
        - This app contains two models called `WishList` and `WishListLineItems`. This allows the user to save items to a list for later purchase.

        - `WishList` is connected to the User model through a OneToOneField which distinguishes which user is saving items to their list. It is also connected to the product model through a ManyToMany field which also the user to choose these products for their list.
        - `WishlistLineItem` is connected to the `Wishlist` and the `Products` model through a foreign key. Due to using a through in the  `WishList` model, the items from that model and passed through this model to be displayed.



[Back to Top](#table-of-contents)

# Technologies Used

-   ## Programming Languages, Framworks and Editors
    -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    -   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   [JavaScript](https://en.wikipedia.org/wiki/JavaScript) 
    -   [Python](https://www.python.org/)
    -   [JQuery](https://jquery.com/)
    -   [Django](https://www.djangoproject.com/)
    -   [Git](https://git-scm.com/)
    -   [Github](https://github.com/)

-   ### Tools Used:
    -   [Heroku](https://www.heroku.com/)
    -   [AWS S3 and IAM](https://aws.amazon.com/)
    -   [Stripe](https://stripe.com/gb)
    -   [Bootstrap](https://getbootstrap.com/)
    -   [PostgreSQL](https://www.postgresql.org/)
    -   [Balsamiq](https://balsamiq.com/)
    -   [Google Fonts](https://fonts.google.com/)
    -   [Font Awesome Icons](https://fontawesome.com/)

[Back to Top](#table-of-contents)

# Features 

## Existing Features

- Index/Home page
    - When a user first enters the site, they are greeted with a welcome title and a site banner.
    - The site banner has information about the site's review score, free delivery, and how to get in touch(maybe).
    - As the user scrolls down, they can read short bits of information about the site.

    <img src="docs/readme/home.png">    

- Navigation Bar
    - The top navigation bar has a site name, search bar, my account, wishlist, and a basket icon as its elements.
    - The site name takes you home.
    - Search bar lets you search all items on the site, using keywords in their product name or description.
    - My Account lets you log in or register your account.
    - Clicking on the wishlist only takes you to the wishlist page if you are logged in. Otherwise, it takes you to the sign-in page.
    - The basket icon takes you to your current shopping basket.
    - The lower part of the navigation bar has the main site product groups, clicking on them brings up a dropdown menu with more product category options.

    <img src="docs/readme/navbar.png">

    - Logged-in users have additional options in my account, such as to log out or to view your profile. Superusers also have the additional option of product management.

    <img src="docs/readme/logged-in-accounts-menu.png">

    - The product navigation bar has various dropdown menu options, and the all products tab has options that are filtered accordingly by name e.g. by price(high - low), etc.
    - The other options represent each product group and their subgroups which match their product description. e.g the skate has all products that are electric skateboards and their various brands.
    - Each navbar option can also take you to all the products that satisfy that group's product type and can be filtered even more.
    
    <img src="docs/readme/all-products-menu.png">

    <img src="docs/readme/group-menu.png">    

- Home page information
    - The home page has very brief snippets of information about the site.

    <img src="docs/readme/home-info.png"> 

- Footer 
    - Here the user can find out more about the developer with links to their social accounts.
    - There is a form where the user can leave them email to sign up for the sites newsletter.
    - The user is the informed if they have been successfully signed up to the newsletter.

    <img src="docs/readme/footer.png"> 

- The register/login page
    - The registration/login pages use the Django-allauth package. The forms used are extended from the respected allauth templates and styled with crispy forms.
    - These forms have validations that tell the user if any data they entered is invalid.

    <img src="docs/readme/"> 

- The Product/Store Page
    - The store pages have various filter options in place. They are categorized by price, rating, category, and name.

    <img src="docs/readme/all-products.png"> 

    - On these various pages, the user has options to change that filter according. Each sub-product group also has links to the different categories in that subgroup at the top of the page.

    <img src="docs/readme/product-group-filter.png">

    - When using the search bar, the user can see the result of their search directly on the page and an option to return to the all products page.

    <img src="docs/readme/product-search.png"> 

- The Product Details Page

    - When a product is clicked on, the user is taken to that product's full details page. There the user has the option to choose the quantity and add the item to their basket, logged in users have the additional option to add the item to their wishlist.
    - Superusers have the additional option to edit/delete products.

    <img src="docs/readme/product-details.png">

    - Logged-in users also have the option to leave a review, whereas guests are given the message to sign in or register an account to be able to do so.
    - To leave a review a title, body, and rating is needed and on success is displayed on the same page.

    <img src="docs/readme/product-review.png">

- Product Management 

    - Superusers have the option to add/edit products on the store.
    - There are options to take the superuser to these edit pages from the all products page or the product details page.
    - On success, they are redirected to the product details page for that item.

    <img src="docs/readme/edit-product.png">

- Profile

    - Users can navigate to this page through my account in the navigation bar.
    - Here the user can update their shipping/billing information.
    - There is also a summary of the user's transactions.

    <img src="docs/readme/profile.png">

- Wishlist

    - This page displays all the items the user has added to their wishlist.
    - Only logged-in users can add items to their wishlist.
    - They can do so from the products or the products details page.
    - This page can be navigated from the main nav at the top.
    - On this page, a user can remove these items from their wishlist or click on them and add them to their basket. 

    <img src="docs/readme/wishlist.png">

- The Basket

    - After adding an item to the basket the user can navigate using the basket icon or the toast to the basket view.
    - Here the user can see a summary of all the items currently in their basket.
    - They can update the quantity of the product and delete the product from their basket.
    - There is also a summary of the costs and buttons to either go back to the store or proceed to checkout.

    <img src="docs/readme/basket.png">

- Checkout

    - Here the user can fill in their billing/shipping details to proceed with the transaction.
    - A basket summary is also present.
    - A logged-in user also has the option to save their entered details to the user's profile.
    - Stripe was used as the payment method for this site.
    - On checking out an overlay covers the screen as the information gets checked by stripe.

    <img src="docs/readme/checkout.png">

    <img src="docs/readme/overlay.png">

- Checkout Success

    - On success, the user is taken to a success page showing a summary of the information entered.
    - An email is also sent to the user using Django and Gmail. Giving them a copy of the transaction details.

    <img src="docs/readme/checkout-success.png">

- Toasts 

    - The site uses toasts from bootstrap to display all the relevant messages/actions from the site.
    - There is a toast for success, info, errors, and warnings.
    - These toasts inform the user of different actions, such as displaying when items get successfully added to the basket.

    <img src="docs/readme/toast-success.png">

[Back to Top](#table-of-contents)

## Features left to Implement

-   Possible features to add in future updates:
    -   Add pagination for comments and products page for better user experience.
    -   Ability for users to delete their account.
    -   Have a group in the navigation bar for new items, items on sale, etc.
    -   Create own unique 404 and 500 error pages to redirect users to.
    -   Use a modal as a confirmation before deleting a product from the site.
    -   Have a custom page/message informing guest users to create an account to use the wishlist feature.
    -   Have an add-to-basket functionality from the wishlist page.
    -   Implement a Django package called MPTT which creates dynamic groups, to create a better grouping of products.
    -   Improve newsletter functionality with mailchimp, have a better success page displaying more information to the user.


[Back to Top](#table-of-contents)

# Marketing

## SEO Research 

-   Research was done to decide what keywords to use to attract protentional customers.
-   Keywords for the site is about the future of personal electric vehicles.
-   The idea of helping the environment by reducing carbon emissions.
-   The idea of enjoying your daily commute more.
-   Being in less traffic.
-   Exploring your surrounding more, taking journeys you wouldn't normally take.
-   To attract the board sport enthusiasts.
-   A markup Facebook page was created for the fictional store.

   <img src="docs/readme/facebook-template.png"> <img src="docs/readme/seo.png"> 

# Testing

## User Stories Testing

-   First Time Visitor/User Goals

    -   As a first User, I want to be able to easily navigate the site.
    
        -   When the visitor first enters the site they are greeted with a welcome message.
        -   The homepage has brief information snippets about the site.
        -   The user can browse by price, category, rating, or by different product groups.

    -   As a first-time user, I want to have the ability to register on the site.

        -   There is my account on the navbar which gives options for the user to log in or register.
        -   When a user views a product detail page they can view the product reviews but would need an account to post one. The relevant links can be found on that page to do so.
    
    -   As a first-time user, I want to view the complete store content.

        -   The user can view all content on the site with the relevant filter options.

    -   As a first-time user, I want to be able to purchase items.

        -   The new user can purchase items on the site without the need for an account.
        -   They would need to create an account to save their shipping/billing details.

-   Returning Registered User Goals

    -   As a registered user, I want to have the ability to log in to the site with my credentials.

        -   The user can do so from the navigation bar.
        -   Or from any product details page, which requires them to log in to post a review.

    -   As a registered user, I want to be able to purchase items.

        -   They can do so with additional benefits.
    
    -   As a registered user, I want to be able to save items for later purchases.

        -   Users have an option to do so from the all products view or the product details page.
        -   They can view them in the wishlist icon in the navbar.

    -   As a registered user, I want to be able to edit/save any information I entered Prior.

        -   The user can do so and have the additional option to save their information to their profile.
        -   This creates a faster checkout process in the future.

    -   As a registered user, I want to have the ability to log out of the site. 

        -   From the navigation bar, the my account dropdown gives the user the logout option.

-   Frequent User Goals

    -   As a frequent User, I want to easily find any new updates to the site.

        -   When viewing the all products page the newest items are always displayed first.

    -   As a frequent User, I want to easily purchase an item with previous information saved.

        -   Registered users who have saved their information on checkout can use the same information on their next purchase.
        -   This creates a faster checkout option for users.

-   Administrator User Goals

    -   As an Administrator, I want to be able to access the Administration panel.

        - They can access this Django admin page by typing /admin at the end of the site name and login in with their credentials.
        -   Here they can edit all aspects of the site, from users, products, and orders.

    -   As an Administrator, I want to have the ability to manage site products.

        -   They can do so from the Django admin or the site itself.
        -   There are options to edit/delete products from the all products page and the products details page.
    
    -   As an Administrator, I want to be able to give other users administrator abilities to help maintain the site

        -   Admins can give other users superuser permissions from the Django admin sections.
        -   This gives more users the ability to maintain the site.

[Back to Top](#table-of-contents)

## Code Validation 

-   HTML

    -   Used [W3C Validation](https://validator.w3.org/) to validate the HTML code.

    <img src="docs/readme/html-validator.png">

-   CSS

    -   Used [(jigsaw) validatior](https://jigsaw.w3.org/css-validator) to validate the CSS code.

        <img src="docs/readme/css-validator.png">

-   JavaScript

    -   [JSHint](https://jshint.com/) was used to check for any major errors in the scripts.

-   Python Code

    -   No errors were returned when testing python code with [PEP8](http://pep8online.com/)
    -   Except for some instances where imports were asking for docstrings in GitHub and class 'x' has no 'DoesNotExist' member which is a warning from pylint. 
    -   Django adds the `objects` and 'DoesNotExist' properties to all model classes, so the IDE isn't aware of this.
    -   This happens in the `update_total` and `save` in the `checkout` app. At this stage, the code is inert as these lines currently have no use. These functions can be updated in the admin when an order is placed. The order can be accessed in the admin and can be adjusted successfully which shows that everything is working as intended.
    -   These changes appear in the user's order as intended.

## Manual Testing

Google Chrome developer tools were used throughout the development process to test breaking points in the site.

-   Toasts
    - The site uses bootstrap toasts to display relevant validation inputs on the site.
    - Success toast appears when items are added to the basket, removed from the basket, logged in, and much more.
    - Info toast displays when editing products, viewing past orders, etc.
    - Error toast displays if any input was incorrect such as entering nothing in the search bar.

    <img src="docs/readme/success-toast.png"> <img src="docs/readme/info-toast.png"> <img src="docs/readme/error-toast.png"> 

-   Navigation Bar
    - Navigation bar is responsive to different screen sizes. It is fully displayed on large to medium screens and then condenses into icons for smaller screens.
    - All links correctly redirect the user to the corresponding pages.
    - Users logged in can see the option to view their profile and log out.
    - Superusers can see the additional option to manage products.

-   Footer
    - Links redirect to the correct social media on a new page.
    - Mailchimp was used to get the users email and to add them to the sites newsletter.
    - After subscribing to the newsletter, a pop up infroms the user they have been added to the newsletter list.
    - This is reflected in mailchimps contacts overview.

-   Products
    - The default all products page displays products by the date they were added.
    - Products that are not active can only be viewed in the Django admin.
    - They are displayed on cards and show the item's name, prices, rating, and a link to their category.
    - Logged-in users have the additional option to add the item to their wishlist.
    - Superusers have the additional option to edit/delete the products.

-   Product details
    - These pages have the same information as the general all products page with the addition of adding the item to the shopping basket.
    - Product details match the information in the database and get displayed correctly.
    - Quantity buttons works, can't go less than 0 or higher than 20.
    - Add to wishlist is only displayed for logged-in users.
    - If an item is not in stock a message gets displayed successfully and only logged users can add these items to their wishlist.
    - The add to basket button gets removed if these conditions are met. 

    <img src="docs/readme/product-not-in-stock.png">

-   Reviews
    - Displays all reviews made for that product and displays a message if they are no reviews made.
    - Users can only post a review if logged in.
    - The logged-in user has the option to edit their review or even delete it if they choose. But, only if they were the user who created it.
    - Superusers have additional permission to edit or delete and review made.
    - Edit review uses the same form as add review and the data gets populated correctly.
    - The toasts successfully display the messages to the page depending on what actions are being done.

    <img src="docs/readme/edit-review.png">  <img src="docs/readme/review-options.png"> 

-   Wishlist
    - Confirmed only logged-in users can this feature.
    - If empty a message gets displayed with a link to the store.
    - Guest users are redirected to the sign-in page if they click on the wishlist.
    - Removing items from their wishlist works correctly.
    - Toast uses info class to tell the user which item was entered into the wish list and when it was removed.

-   Basket
    - Icon in the navigation bar takes the user to the basket. The basket gets updated when items are added, updated, and deleted.
    - Basket icon changes color when items are added to the basket.
    - Quantity buttons here reflect the quantity added from the product details page.
    - Basket gets updated when adjustments are made here.
    - Items in the basket remain when the user logs in beforehand. Sign the session data is kept stored correctly.
    - Correct totals and subtotals are correct.
    - Free delivery is being calculated correctly. 

-   Checkout
    - Item data is the same as the basket page.
    - Form validation works and informs what error is being made.
    - Stripe correctly displays if the order is successful.
    - Users' billing/shipping details get populated if it was saved previously. 
    - Stripe test card input `4242 4242 4242 4242` works when completing an order.
    - Overlay covers the screen when information is entered.
    - An error in the card information displays correctly.
    - Success toast displays with the order number on successful payment.
    - Redirects to checkout success page if form validation matches stripes.
    - Stripe webhook shows if the order was created from the database or had to be created from the webhook data on stripes payment intent succeeded event with 200 responses.
    - An email successfully gets sent to the user about order details.

    <img src="docs/readme/stripe.png"> 
    
    <img src="docs/readme/confirmation-email.png">

-   Admin
    - Only admins have access to the product management page from the my account dropdown.
    - Only admins can see and use the edit/delete products.
    - Product management goes to the correct page to add an item.
    - The correct details appear from the database in the form when editing a product.
    - Toasts successfully appear when the superuser is editing a product, editing a product, and deleting a product.

-   Product Management
    - Product successfully gets added to store using the form.
    - Products can be edited and changes display correctly.
    - Form validation works when the field is required.
    - Gets directed to the product details page after adding/editing a product.
    - Toast informs users accordingly.

-   Search 
    - Search parameters work accordingly.
    - Search finds keywords from the product name or description.
    - Results for the search are displayed for the user.

-   Heroku Config Vars
    - Variables stated in the Heroku config vars are working accordingly.
    - Static files are successfully updated to AWS when files are committed to Heroku.
    - Email variable works as emails get sent to the user on successful order.
    - Stripe is connected correctly as 200 responses post in developers' webhooks on successful orders and more.

    <img src="docs/readme/heroku-config-vars.png">

[Back to Top](#table-of-contents)

## Automated Testing  

- Not automated testing was done for this project.
- Ideally, class-based views should have been used to make this process more manageable.


# Bugs

-   Users who have items in their basket who then log out lose their items in their basket.
-   Due to the different sizes of the product images used, in the all products view, the images of the different items don't quite match up.
-   After completing the newsletter form the users email remains in the field, until the user refreshes the page.
-   Hompage images are too large and user might not know of content below. Images on change moves the whole page.

# Deployment

The master branch of this repository has been used for the deployment version of this project.

## Github and Gitpod

- The [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template) template was used to develop this project. To use this template:
    - Click `use this template`
    - Create a repository name
    - Click `create a repository from template` to create.
    - After the repository is created, click on gitpod to open the workspace.
    It- Best to pin this workspace to your Dashboard for convenience.
    - Committing changes should be done often with:
        - `git add` adds all modified files to the staging area.
        - `git commit -m "A message explaining commit"` commits changes with a message.
        - `git push` pushes all committed changes to the GitHub repository

- Forking the GitHub Repository

    - If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

    - Find the relevant GitHub repository
    - In the top right corner of the page, click the Fork button (under your account)
    - Your repository has now been 'Forked' and you have a copy to work on
    - Cloning the GitHub Repository

- Cloning your repository will allow you to download a local version of the repository to be worked on. Cloning can also be a great way to backup your work.

    - Find the relevant GitHub repository
    - Press the arrow on the Code button
    - Copy the link that is shown in the drop-down
    - Now open Gitpod & select the directory location where you would like the clone created
    - In the terminal type 'git clone & then paste the link you copied in GitHub
    - Press enter and your local clone will be created.

## Deployment to Heroku

- Followed the steps from the [Code Institute](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf) document.
- Use `pip3 freeze --local > requirement.txt` to create a list of packages for Heroku to install for your app.
- From Heroku create a new app with the region closest to you.
- Then enter the resources tab and install Heroku Postgres.
- Navigate to the settings tab and under config vars, set them according to the same variables listed in your own workspace.
- Due to a breach of security the project needs to be deployed using the Heroku CLI from the workspace:
    - Login to heroku `heroku login -i`
    - Enter your email and password.
    - Connect to Heroku git remote with `Heroku git: remote -a APPNAME`
    - Push to Heroku with `git push Heroku main`

[Back to Top](#table-of-contents)

# Credits

- [Overstackflow](https://stackoverflow.com/) for troubleshoot advice.
- [Code Institute](https://github.com/dhowai/boutique-ado) for their eccommence site lessons.
- [Overstackflow](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1629319398268100) for wishlist app concept.

## Media

- [Unsplash](https://unsplash.com/) for homepage images.
- [Ride and Glide](https://www.rideandglide.co.uk/) for the product images.
- Startbootsrap for verious templates [products](https://startbootstrap.com/template/shop-homepagehttps://startbootstrap.com/template/shop-homepage) [Shop-item](https://startbootstrap.com/template/shop-item) [homepage](https://startbootstrap.com/template/scrolling-nav)
- [Bootdey](https://www.bootdey.com/snippets/view/shopping-cart-checkout#html) for shopping cart format. 

# Acknowledgements

-   The students on Slack for peer review
-   The tutor support provided by Code Institute

[Back to Top](#table-of-contents)