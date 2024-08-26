<p align="center"><img src="/static/favicon/android-chrome-512x512.png"/></p>

<br>
<br>

# Celestial**Craft**

<br>

*CelestialCraft is an e-commerce platform dedicated to bringing the beauty and artistry of handmade crafts and artisanal goods to a global audience. Our store is a haven for those who appreciate the time-honored traditions of craftsmanship and the unique touch of human creativity. Here, customers can discover a wide range of meticulously crafted items, from elegant home decor to bespoke accessories and personalized gifts.*

<br>

## Table of Contents

<br>

- [Project Overview](#project-overview)
- [Live Site](#live-site)
- [Repository](#repository)
- [Author](#author)
- [Target Audience](#target-audience)
- [Project Goals](#project-goals)
- [User Stories](#user-stories)
- [Developer](#developer)
- [Design choices](#design-choices)
- [Wireframes](#wireframes)
- [Features](#features)
- [Interactive Design Elements](#interactive-design-elements)
- [Implemented features](#implemented-features)
- [Future features](#future-features)
- [Version Control](#version-control)
- [Testing](#testing)
- [Accessibility Testing](#accessibility-testing)
- [Examples of Responsive design](#examples-of-responsive-design)
- [Defects list](#defects-list)
- [Technologies used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)


<br>

## Project Overview

<br>

![Mock up](/static/images/mockup.png)

This site provides a seamless shopping experience for craft enthusiasts, home decorators, and gift shoppers, featuring a range of items such as art, homeware, and furniture. The platform is designed with a user-friendly interface, mobile responsiveness, and secure payment integration, ensuring an enjoyable and reliable shopping experience.

<br>

## Live Site

- https://celestial-crafts-043fbda6275e.herokuapp.com/

<br>

## Repository

- https://github.com/MrHraza/Celestial-Crafts

<br>

## Author

Developer  -  *Husnain Raza*

<br>

## Target Audience

<br>

The target audience for Celestial Crafts includes craft enthusiasts, home decorators, and gift shoppers who appreciate unique, handmade, and artisanal products. These individuals are likely interested in high-quality, aesthetically pleasing items that add a personal touch to their homes or make thoughtful gifts.
  
<br>

## Project Goals

<br>

1. **Showcase Skills:** Demonstrate skills using coding languages; html, css, javascript, python, flask, jinja.

2. **User-Friendly Design:** Create an appealing website layout that ensures easy navigation for visitors, allowing them to access information effortlessly.

3. **Mobile Responsiveness:** Ensure the website is responsive across various devices, including smartphones, tablets, and desktops, optimizing the user experience for all visitors.

4. **Call-to-Action (CTA):** Include clear call-to-action elements, such as a stripe payment method or buttons and prompting visitors to engage further.
   
<br>

## User Stories

<br>

*Visitor*

> As a visitor, I want to browse different categories of crafts so that I can find products that interest me.

*Customer*

> As a customer, I want to search for products by name or keyword so that I can quickly find what I'm looking for.
> I want to view product details, including images, descriptions, and prices, so that I can make an informed purchase decision.
> I want to add products to my shopping bag so that I can review them before purchasing.
> I want to proceed to checkout and enter my payment information so that I can complete my purchase.
> I want to save items in my cart for later so that I can purchase them in the future.

*User*

> As a user, I want to log in to my account so that I can manage my profile and view my order history.
> I want to register an account so that I can save my details for future purchases.
> I want to access the website on my mobile device so that I can shop on the go.

*Admin*

> As an admin, I want to add, edit, or delete products so that I can manage the inventory on the website.


<br>

## Developer

<br>

As a Developer I want to push myself and demonstrate my ability with different coding languages in combination.

<br>

## Design choices

<br>

#### Colours

In this project the color palette consists of black, white, light brown, and dark brown. This in my opinion was a strong and thoughtful choice for the following reasons; 

- **Warm and Earthly tones**: Light brown and dark brown evoke a sense of warmth, comfort, and nature. These colors are associated with organic materials like wood, leather, and earth, which align perfectly with a crafts website that focuses on handmade, artisanal products.

- **Proffessional and Timless contrast**: The Black and White combination ensures that the website looks polished and organized, which is important for user experience and readability.

- **Emotional and Psychological Impact**: Dark brown is often associated with reliability, stability, and support, which are great qualities to convey in a business centered on handmade products. It can give customers the impression that your products are made with care and attention to detail.


<br>

#### Typography

I used one font throughout for its populatrity in webdesign, 'Lato'.

**Lato:**

- The font's design strikes a balance between being friendly and approachable while maintaining a professional tone.
- I found that it has been designed with excellent readability in mind, both at small and large sizes. Its clean lines and balanced proportions ensure that text remains legible across different devices and screen resolutions. 
- The font’s letter spacing and weight distribution make it easy on the eyes, which enhances the user experience.
- Lato was designed specifically for the web, so it renders well across different browsers and operating systems.

<br>

#### Imagery

Seven images in total, a background on the homepage and six products displayed on the products page can be seen on the website.

<br>

#### Site Structure

I have opted for a multi-page website as this offers flexibility, organization, and scalability.

<br>

## Wireframes

<br>

- desktop homepage

![desktopwireframe](/static/images/desktop-homepage.jpg)

- desktop products

![desktopwireframe](/static/images/desktop-products.jpg)

- desktop product details

![desktopwireframe](/static/images/desktop-product-details.jpg)

- desktop shopping cart

![desktopwireframe](/static/images/desktop-shopping-cart.jpg)

- phone homepage

![phonewireframe](/static/images/phone-homepage.jpg)

- phone products-page

![phonewireframe](/static/images/phone-products-page.jpg)

<br>

## Features

<br>

From the user stories I have understood that what the client requires is a website that showcases the following:

*Clean and Intuitive Design:*
- Visually appealing layout with adequate white space. Easy-to-read font and appropriate font sizes. Consistent color scheme that complements the content.

*Clear Navigation:* 
- Intuitive menu or navigation bar for easy access to different pages. Ability to Search and item.
  
*Different pages:* 
- Namely; Products, Shopping bag, Checkout & Login.

*Visual Enhancements:*
- High-quality images, that are relevant and add value.
  
*Mobile Responsiveness:*
- Optimized for various devices, ensuring a seamless experience on mobile.
  
*Social Media Integration:*
- Links to relevant social media (Twitter, facebook, Instagram etc.).

*Call-to-Action (CTA):*
- A clear CTA for users i.e Secure Payment system.

<br>

## Interactive Design Elements

<br>

**Menu**  
- Hovering over a menu item *subtly* (see 'Art > Sculptures') hightlighted item.

![menu](/static/images/menu.png)

- Menu is condensed to a dropdown on smaller screens. (see hamburger icon)

![smallscreen-menu](/static/images/smallscreen-menu.png)


**Buttons** 
- Working/linked buttons are used on the website (see 'browse shop' which is linked to the products page).

![buttons](/static/images/browseshop-button.png)

**Search bar** 
- Working search feature to quickly navigate the products.

![search bar](/static/images/searchbar.png)

Search results.

![search results](/static/images/searchresults.png)


**Stripe Element**
- This is a working stripe element that is connected to stripe and is allowing purchases to be made, it also has a record of purchases made.

![stripe element](/static/images/stripe-element.png)

Then sent.

![stripe web](/static/images/stripe-paid.png)


**Social links**
- Celestialcrafts socials can be found in the footer.

![social links](/static/images/social-links.png)

**Sign-up/Login**
- Sign-up form 

![signup](/static/images/signup.png)

- Login form

![loginform](/static/images/login.png)

- once you have logged in, 'My Account' on the navigation area is replaced with your username.

![loggedin](/static/images/loggedin.png)

<br>

## Implemented features

<br>

**header**
- This contains a navigation element in the form of a menu. When browsing the website on a tablet or a mobile device this changes to a drop-down menu.
  
**Products page**
- Features a catalogue of products.
  
**Checkout page**
- Features a Stripe element.

**User accounts**
- Sign up, login and create a profile.
  
**Store Manager**
- Once the store owner/admin logs in, additional menu links are accessable to add/edit/delete products.
  
**footer with socials.**
- Social links to website's social media platform.

<br>

## Future features

<br>

1. Customer Reviews and Ratings: Allow customers to leave reviews and rate products, which can help build trust and provide valuable feedback for other shoppers.

2. Wishlist Functionality: Enable users to save items to a wishlist for future purchases, enhancing user experience and increasing potential sales.

3. Advanced Search and Filters: Improve the search functionality with advanced filters (e.g., by price, category, popularity, or availability) to help users find products more easily.

4. Product Customization Options: Allow customers to customize products (e.g., choosing colors, adding engravings) for a more personalized shopping experience.

5. Gift Wrapping and Message Options: Provide an option for customers to add gift wrapping and a personalized message to their orders, ideal for gifts.

6. Multiple Payment Gateways: Expand payment options to include digital wallets like Apple Pay, Google Pay, or cryptocurrency, offering more flexibility to customers.

7. Email Notifications and Marketing: Implement automated email notifications for order confirmations, shipping updates, and abandoned carts, as well as targeted marketing campaigns.

<br>

## Version Control

<br>

Version control for this project was managed using Git and GitHub. Git was used via the terminal in gitpod.io to commit changes.

#### Commit Habits

Commits were made throughout the development process to ensure that changes were tracked effectively. This approach not only provided a clear history of the project's progression, but also ensured that any changes could be rolled back if necessary.

#### GitHub 

GitHub was used as the remote repository for storing the project's code and resources. It provided a backup of the project and allowed it to be accessed from different locations.

#### Contributors

I am the sole developer of this project.

<br>

## Testing 

### HTML validation

<br>

- Homepage

![homepagehtmltest](/static/images/homepage-validation.png)

- products

![productlisthtmltest](/static/images/productlist-validation.png)

- product details

![productdetailhtmltest](/static/images/products-detail-validation.png)

- product details

![productdetailhtmltest](/static/images/products-detail-validation.png)

- checkout

![checkouthtmltest](/static/images/checkout-validation.png)

- shopping bag

![shoppingbaghtmltest](/static/images/shopping-bag-validation.png)

<br>

#### Errors in validation

<br>

> The following errors (see screenshots), I couldn't find these errors in the html.

1. The pages extend base.html, but the error is shown saying I need "!doctype html" which I have included in base.html.
2. This shows that I have a div element as a child of h1 however looking through the code I did not find this.
3. This is telling me I have an empty h1. I also could not see this.  


- add product page

![add product](/static/images/add-product-validation.png)

- edit product page

![edit product](/static/images/edit-product-validation.png)

- delete product page

![delete product](/static/images/delete-product-validation.png)

- profile page

![profile](/static/images/profile-validation.png)

<br>

### CSS validation

<br>

- base.css

![projectcssfile](/static/images/css-validation.png)

<br>

### PYTHON validation

<br>

#### Home app

- urls.py

![homeurls](/static/images/home-urls.png)

- views.py

![homeviews](/static/images/home-views.png)

#### Products app

- forms.py

![productforms](/static/images/product-forms.png)

- models.py

![productmodels](/static/images/product-models.png)

- urls.py

![producturls](/static/images/product-urls.png)

- views.py

![productviews](/static/images/product-views.png)

#### Bag app

- bag-operations.py

![bagoperations](/static/images/bag-operations.png)

- bag-context-processors.py

![bagcontextprocessors](/static/images/bag-context-processors.png)

- bag-urls.py

![bagurls](/static/images/bag-urls.png)

- bag-views.py

![bagviews](/static/images/bag-views.png)

#### Checkout app

- checkout-views.py

![checkoutviews](/static/images/checkout-views.png)

- checkout-admin.py

![checkoutadmin](/static/images/checkout-admin.png)

- checkout-urls.py

![checkouturls](/static/images/checkout-urls.png)

- checkout-models.py

![checkoutmodels](/static/images/checkout-models.png)

- checkout-forms.py

![checkoutforms](/static/images/checkout-forms.png)

#### Profiles app

- profile-forms.py

![profileforms](/static/images/profile-forms.png)

- profile-apps.py

![profileapps](/static/images/profile-apps.png)

- profile-models.py

![profilemodels](/static/images/profile-models.png)

- profile-signals.py

![profilesignals](/static/images/profile-signals.png)

- profile-urls.py

![profileurls](/static/images/profile-urls.png)

- profile-views.py

![profileviews](/static/images/profile-views.png)

<br>

## Accessibitily Testing

<br>

### colour contrast

<br>

![colourcontrast](/static/images/colour-contrast.png)

<br>

### Lighthouse

<br>

- homepage desktop 

![lighthouse desktop](/static/images/homepage_desktop.png)

- product listing desktop 

![lighthouse desktop](/static/images/product_listing_desktop.png)

- product detail desktop 

![lighthouse desktop](/static/images/product_detail_desktop.png)

**Lighthouse Phone Performance**

**Note: my computer is slow and is always near 100% cpu usage, I consistantly get high cpu usage notifications. I tried using smaller file sizes for both the homepage and product listings. Also I googled ways to increase performance to no avail.**

- homepage phone

![lighthouse phone](/static/images/homepage_phone.png)

- homepage phone

![lighthouse phone](/static/images/product_listing_phone.png)


### General testing

<br>

- Desktop

| Aspect        | Result         | Comment  |
| ------------- |:-------------:| -----:|
| Webpages load | Yes |  |
| Layout appearances are correct | Yes |  |
| Scroll works | Yes |  |
| Logo link works | Yes |  |
| All menu links work | Yes |  |
| Hover features work | Yes |  |
| Buttons work | Yes |  |
| Forms work | Yes |  |
| Footer links work | Yes |  |
| Login/Logout function works |  Yes  |    |
| Shopping bag functions work | Yes | |
| Checkout functions work (stripe) | Yes | |
| Notifications appear | Yes | |
| Details can be saved to profile | Yes | |
| Order history feature works | Yes | |
| Management features work | Yes | |
| Images load correctly  | Yes | |
| Django backend admin feature work | Yes | |

<br>

- Mobile

| Aspect        | Result         | Comment  |
| ------------- |:-------------:| :----- |
| Webpages load | Yes | The webpages load slower than desktop |
| Layout appearances are correct | No | On small devices layout could be better |
| Scroll works | Yes |  |
| Logo link works | Yes |  |
| All menu links work | Yes |  |
| Hover features work |  | No (unable to hover on mobile) |
| Buttons work | Yes |  |
| Forms work | Yes |  |
| Footer links work | Yes |  |
| Login/Logout function works |  Yes  |    |
| Shopping bag functions work | Yes | |
| Checkout functions work (stripe) | Yes | |
| Notifications appear | Yes | |
| Details can be saved to profile | Yes | |
| Order history feature works | Yes | |
| Management features work | Yes | |
| Images load correctly  | Yes & No | on the smallest screen images don't load correctly |

<br>

## Examples of Responsive design

<br>

- laptop

![Laptop view](/static/images/laptop-view.png)

- Ipad Air

![ipad air](/static/images/ipad-air.png)

- iphone xr

![iphone xr](/static/images/iphone-xr.png)

- samsung galaxy A51

![samsung galaxy A51](/static/images/samsung-galaxy-a51.png)

- samsung galaxy s8

![samsung galaxy s8](/static/images/samsung-galaxy-s8.png)

<br>

## Screenshots

<br>

- homepage-statement

![homepage-statement](/static/images/homepage-statement.png)

- homepage

![homepage](/static/images/homepage.png)

- menu-open

![menu-open](/static/images/menu-open.png)

- order-history

![order-history](/static/images/order-history.png)

- order-success

![order-success](/static/images/order-success-notification.png)

- payment

![payment](/static/images/payment.png)

- product details

![product-details](/static/images/product-details.png)

- products

![products](/static/images/products.png)

- searched-item

![searched-item](/static/images/searched-item.png)

- shopping-bag

![shopping-bag](/static/images/shopping-bag.png)

- user-options

![user-option](/static/images/user-options.png)


<br>

## Defects list

<br>

*On smaller screens the layout could do with some more organising, for a more user friendly experience.

<br>

## Technologies used

#### Programming Languages

<br>

- CSS 
- HTML 
- Jinja
- Python
- JS 
- Django
- Markdown

<br>

#### Frameworks and Extensions

<br>

- Bootstrap 4.7.0

<br>

#### Icons

<br>

- FontAwesome 4.7

<br>

#### Tools

<br>

- Github
- Gitpod
- Visual Studio
- Pen and paper
- Internet
- Markdown table of contents generator
- Favicon

<br>

## Deployment

<br>

### Creating a Gitpod Workspace

The project was created in Gitpod using the Code Institute Gitpod Full Template using these steps:

1. Log in to GitHub and go to the [Code Institute student template for Gitpod](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this Template' next to the Green Gitpod button.
3. Add a repository name and click 'Create reposiory from template'.
4. This will create a copy of the template in your own repository. Now you can click the green 'Gitpod' button to open a workspace in Gitpod.

### Forking the GitHub Repository

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/MrHraza/celestialcrafts)
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

You will now have a fork of the repository, but you don't have the files in that repository locally on your computer.

To make a local clone:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/MrHraza/celestialcrafts)
2. Above the list of files, click  Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the 'Copy' icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the 'Copy' icon. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the 'Copy' icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub AE username instead of YOUR-USERNAME:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Celestial-Crafts`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo) for the GitHub quick start guide with images and more detailed explanations of the above process.

### Creating a database

You will need to create a database, unless you wish to pay for a Heroku database.

1. Go to [ElephantSQL.com](https://elephantsql.com/) and select create a database
2. Select the free database plan
3. Select “Log in with GitHub” and authorise with GitHub
4. Create new team form. You can use your name, read and agree to the T&C's, select yes for GDPR, provide your email address and click Create Team. Your account will be created 
5. From your dashboard, click “Create New Instance”
6. Set up your plan. Give it the same name as your project, select the free plan. Select "select region" and select a region close to you.
7. Click review, and if the details are correct, click create instance.
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, clicking the copy icon will copy the database URL to your clipboard

### Creating an application with Heroku

You will need to deploy the application using Heroku.

1. Create a Heroku account and log in.
2. Create a new app. When you do so, select the closest region to you and give it an appropriate name. Note Heroku names must be unique
3. In your app Settings, add the config var DATABASE_URL, and for the value, paste in your database url from ElephantSQL.
4. In your app Settings, add the config var DJANGO_SECRET_KEY. Generate a DJANGO_SECRET_KEY and paste it in. Keep this secret.

### Project preparation in Gitpod - Connect to your external database

1. In Gitpod, install dj_database_url and psycopg2 by running this command in the terminal
```pip3 install dj_database_url==0.5.0 psycopg2```
2. Update your requirements.txt file with the newly installed packages by running this command in the terminal
```pip freeze > requirements.txt```
3. In the project settings.py file, paste the following lines of code underneath the import for os
 ```import os```
 ```import dj_database_url```
4. Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated. Do not commit this as it will reveal sensitive information.
```# DATABASES = {...}```
 ```DATABASES = {'default': dj_database_url.parse('your-database-url-here')}```
5. In the terminal, run the showmigrations command to confirm you are connected to the external database. You should see a list of all migrations printed to the terminal
 ```python3 manage.py showmigrations```
6. Migrate your database models to your new database by running:
```python3 manage.py migrate```
7. Create a superuser for your new database with the following command (Follow the steps to create a your superuser username and password. The email address can be left blank.):
```python3 manage.py createsuperuser```
8. Now you can delete the code you copied in step 4 and uncomment out the original Database code.
```DATABASES = {...}```

### Deploying to Heroku

1. In Gitpod, install Gunicorn by running: 
```
pip3 install gunicorn
```
2. Update your requirements.txt file to include this:
```
pip freeze > requirements.txt
```
3. Create a Procfile. Open it and ensure it doesn't have a new line, as this can create errors. Ensure it starts with a capital P.
4. In your Procfile, enter:
```
web: gunicorn Celestialcrafts.wsgi:application
```
5. In the terminal, run the following and log into Heroku:
```
heroku login
```
6. Temporarily disable collect static by running:
```
heroku config:set DISABLE_COLLECTSTATIC=1
```
7. Update the hostname of your Heroku app to ALLOWED_HOSTS in settings.py
8. Commit your changes and push to Github.
9. Go back to your app on Heroku
10. Deploy your project by going to the Deploy tab and choose 'Connect to Github'
11. Find your repository name and select Connect.
12. Your app should be deployed without any static files.

### Connecting to AWS & creating a S3 bucket

1. Create an AWS account if you don't already have one
2. Go to your AWS account, and go to S3
3. Create a new bucket. Uncheck block all public access and set the Object Ownership settig with ACLs enabled. Click Create Bucket
4. On the properties tab, scroll down to 'static website hosting' and 'use this bucket to host a website'. Set the home/default page to 'index.html' and error link as 'error.html', then save.
5. On the permissions tab, go to 'CORS configuration' and copy in the below.
``` 
[
   {
   "AllowedHeaders": [
   "Authorization"
   ],
   "AllowedMethods": [
   "GET"
   ],
   "AllowedOrigins": [
   "*"
   ],
   "ExposeHeaders": []
   }
   ]
```  
6. On the permissions tab, go to Bucket Policy and copy the ARN
7. Select generate policy. Select S3 Bucket Policy under policy type. Enter * for all Principals, and the action will be GetObject. Paste in the copied ARN into the ARN field.
8. Click add statement then generate policy, and copy this policy into the Bucket policy editor.
9. Before you press save, enter a star after the slash in Resource to allow access to all resources in this bucket. Click save
10. Go to the Access control list (ACL) tab, click edit and enable List for Everyone under the public access section.

### Setting up IAM

1. Go to your AWS account, and go to IAM
2. Click groups and create a new group. Call it something like manage-your-site-name.
3. Go to Policy and create policy. Go to the JSON tab and select import managed policy.
4. In the dialogue box, search for S3 and import the S3 Full Access Policy.
5. Get the ARN from your S3 bucket and paste it into the resources with and without the trailing *. It should look like this:
```
"RESOURCE": [
   "arn:aws....",
   "arn:aws..../*",
]
```
6. Click review policy. Give it a name and description. Click create policy.
7. Go back to groups and click your group to manage it. Go to the permissions tab, open Add Permissions and click Attach Policy. Search for your policy by it's name and select it. Click Add Permissions.
8. Go to Users and click Add User. Name your user something like your-site-name-static-files-user. Give them programmatic access. Select next.
9. Add the user to your group. Click through to the end and click Create User.
10. Download the CSV to get the users access key and secret access key. Ensure you download it now, because you won't be able to access it again.

### Connecting Django to S3.

1. Go to Gitpod. We will need to install 2 packages with the following commands:
pip3 install boto3
pip3 install django-storages
2. Update your requirements.txt file to include this:
```
pip freeze > requirements.txt
```
3. Add ```'storages',``` to your INSTALLED_APPS in settings.py.
4. In settings,py, update the AWS storage bucket name, region key and custom domain to match your own.
5. Go to Heroku. Inside your project, go to the 'Settings' tab. Scroll down and click 'Reveal Config Vars'.
6. Add in the following variables with the relavant values. (Get the Keys from the CSV file). Set USE_AWS to Tue.
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
USE_AWS
```
7. Remove the disable collect static config var from Heroku.
8. Back on Gitpod, git add, commit and push your changes.
9. If your set up was correct, you should see a static folder in your S3 bucket, and your static files being rendered on the live site.

### Adding Media Files & Connecting Stripe

1. In AWS, add a folder called media. Inside it upload any photos you want rendered. In this project, it will be the background splash image, and the holding image.
2. Click next, manage public permissions and select manage public read access to these objects. Click next and upload.
3. In Heroku, under your project settings, add the following CONFIG_VARS with your variables:
```
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
```

<br>

## Credits

<br>

- Code Institute Introduction to frameworks
- Code Institutes Django lessons
- Code institute Project - Boutique ado

<br>

## Content and Media

### Icons

<br>

- https://fontawesome.com/v4/icons/

<br>

### All images were taken from

<br>

- https://stockcake.com/
- www.pngegg.com - Favicon 

<br>

### Code related ideas

<br>

- https://codepen.io
- Code Institutes lessons
- https://www.w3schools.com/
- https://docs.python.org/
- https://docs.djangoproject.com/

<br>

### Acknowledgements
- https://www.site24x7.com/tools/javascript-validator.html
- CodeInstitute template
- **Malia Havlicek - mentor** 
- Chrome Developer Tools
- https://www.siteimprove.com/toolkit/color-contrast-checker/
- https://www.w3schools.com/
- https://slack.com/
- https://ui.dev/amiresponsive
- https://jigsaw.w3.org/css-validator/
- Lighthouse
- Windows screen reader

