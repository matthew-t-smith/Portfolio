# Personal Portfolio

Django Application using Python and JavaScript with a SQLite3 Database

This project was built as a final project for a semester in Web App Development.
  It will now exist as an ever-evolving personal portfolio site.

## Back-End

#### APIs

Google Drive API: Models store files and images in Google Drive, allowing storage
  and recall for loading into templates.

Google Maps API: The contact page displays a map of my current city.

Unsplash API: For backgrounds on the site, the Unsplash API is called with a random
  photo loaded using certain filters. The photo will be new every day.

#### Requirements

The only additional requirement is a library to assist in using Google Drive's API
  inside of Django's models for storage. Unfortunately, I was not able to directly
  load files into the HTML despite a number of trials (`iframe`, reading file in
  `views`, and even a plain `object` tag). Consequently, I used the resulting URLs
  as simple `href` values.

#### Models

`Projects` and `Images` for those projects are kept as two model objects, with the
  images using a foreign key to reference to the corresponding project. README files
  are uploaded for projects as well in hopes of converting to HTML content, but
  there were permission errors that have prevented this so far. As mentioned, files
  are stored in Google Drive via the API.

#### Views

Views are straightforward, only adding objects from the database via `context`.

#### Custom Tag

Under the `portfolio/templatetags/` directory is a file housing a custom tag built
  to add an additional filter to the context images once they reach the HTML. It
  is implemented with a decorator function.

#### JavaScript

The `script.js` file gets used across all pages referencing the `base.html` template.
  It makes sure to load an image from the Unsplash API and place as a background.

`index.js` loads the image into Material Design Lite cards as a background.

`contact.js` has the logic for loading the map from Google's Map API.

## Front-End

At the beginning of this project, Google had not yet released their Material Design
  Revamp that is now available. I intend to update using the Material Design Components
  for Web later, but I continued with the Material Design Lite version for the final
  project submission.

#### Home

The home page has two navigations that change based on the device, either through
  a drawer-only on mobile screens, or both drawer and regular navigation tabs for
  larger screens. Card components represent CV information that include links to my
  LinkedIn profile, specifically to the applicable sections.

#### Projects

A single `project.html` template allows a uniform representation across different
  project categories. As mentioned, the images and README files were not able to
  directly load into the HTML, so for now there are simple `href`s to the URLs.

#### Blog

Once this application is deployed to a URL, I can register with Medium's API and
  post blog entries to this page.

#### Contact

A simple page showing a map of my current city and some basic contact information,
  including a non-robot-sniffing phone number and email address, as well as my
  LinkedIn and GitHub profiles.
