# Food Menu Website

A responsive food menu website created with Bootstrap and JavaScript, featuring a dynamic menu and "Food of the Day" section powered by the Spoonacular API. This project showcases various dishes with their recipes, allows users to contact the restaurant, and provides information about the business.

## Features

- **Home Page**: 
  - Displays a carousel of featured dishes with images and descriptions, dynamically fetched from the Spoonacular API.
  - Contains a "Food of the Day" section showcasing a popular dish, updated daily from the API.

- **Menu Page**:
  - Lists several dishes with images, descriptions, and links to view detailed recipes.
  - Includes a "Load More" button to dynamically display more dishes.

- **About Page**:
  - Provides a brief history, mission statement, and a "Meet the Staff" section.
  - Features a quote from Paul Prudhomme.

- **Contact Page**:
  - A form that allows users to submit their email, name, phone number, and a description for questions or feedback.
  - Includes a rating system where users can rate their experience.

## Pages

1. **Home**: Introduction with a featured dish carousel and "Food of the Day" section.
2. **Menu**: List of all available recipes, loaded dynamically from the Spoonacular API.
3. **About**: Business history, mission, and team introduction.
4. **Contact**: Contact form and user rating system.

## Technologies Used

- **HTML5**
- **CSS3**
- **Bootstrap 5.3.2** (for responsiveness and UI components)
- **JavaScript** (for interactivity)
- **Spoonacular API** (for fetching dish data dynamically)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/food-menu-website.git
    ```

2. Navigate to the project folder:

    ```bash
    cd food-menu-website
    ```

3. Open the `Home.html` file in your browser to view the website. Make sure to replace the API key in the JavaScript file with your own Spoonacular API key.

## Project Structure

```
├── Home.html
├── about.html
├── contact.html
├── menu.html
├── assets
│   ├── images
│   └── css
└── README.md
```

## How to Use

- **Home Page**: Explore the carousel of featured dishes and click "See Recipe" to view detailed recipes. The "Food of the Day" section shows a new popular dish daily.
- **Menu Page**: Scroll through the available dishes and view recipes. Use the "Load More" button to dynamically load more content.
- **About Page**: Learn about the business history, mission, and staff.
- **Contact Page**: Submit inquiries or feedback using the form and rate your experience using the star system.

## Future Enhancements

- Expand the recipe categories and add filters.
- Implement a back-end system for handling form submissions and storing ratings.
- Add infinite scrolling for the "Menu" page, automatically loading more dishes as the user scrolls down.

#
