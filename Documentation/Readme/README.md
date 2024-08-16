<p align="center"><img src="static/favicon/android-chrome-512x512.png"/></p>

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
- [Features](#features)
- [Interactive Design Elements](#interactive-design-elements)
- [Implemented features](#implemented-features)
- [Future features](#future-features)
- [Version Control](#version-control)
- [Defects list](#defects-list)
- [Technologies used](#technologies-used)


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

## Defects list

<br>

*On smaller screens the layout could do with some more organising, for a more user friendly experience.
*Also the accordian on the homepage, on smaller screens could be better.

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