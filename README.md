<h1 align=center> Movies Database Filter </h1>
<h2 align=center> A CSC110 Project by Zachary Breene </h2>
<h4 align=center> Created at The University of Rhode Island, December 2020 </h4>
</n>
<h4 align=center> NO AI WAS USED IN THE CREATION OF THIS PROJECT </h4>
## Introduction
My task for this project was to create a Python-based command-line interface (CLI) program capable of parsing, filtering, and analyzing a text-based database of movies. With the data properly loaded, the program can execute various search queries and can export a sorted version of the database using a custom selection sort algorithm.

---

## Implementation + Functions
### moviefilter.py

This is the main file containing the core logic, calculations, and the interactive CLI menu for the program. </n>

&emsp; ***File Parsing & Loading***

* The script utilizes `openFile()` to safely prompt the user for the database file, catching invalid inputs. The `getMovies()` function then reads the data line-by-line, splitting the comma-separated values into parallel lists for titles, genres, runtimes, ratings, studios, and release years.

&emsp; ***Search & Filter Methods***

* The program features multiple search methods. `findFilmsByStudio()` iterates through the lists to find and format all movies produced by a specific studio. `longestFilmByGenre()` locates the film with the maximum runtime within a specific genre. `findFilmsByRating()` retrieves movies that fall within a specified year range and match a given rating. Finally, `findFilmByTitle()` performs a linear search for an exact movie title match.

&emsp; ***Selection Sort & Export***

* The `sortByYear()` function implements an in-place selection sort algorithm to organize all the parallel lists in chronological order based on the release year. It then writes the newly sorted database out to a user-defined text file.

### movies.txt

This is the dataset used to populate the program. It is a comma-separated text file containing records for 150 unique films, formatted sequentially with fields corresponding to Title, Genre, Runtime, Rating, Studio, and Release Year.

---

## How To Run
If you want to run this program, you must download both the `moviefilter.py` script and the `movies.txt` database file (or provide your own properly formatted comma-separated text file). Ensure both files are located in the same directory. Run the program using a Python 3 interpreter via your terminal or IDE (e.g., typing `python moviefilter.py`). When prompted for the file name at launch, type `movies.txt`. From there, you can interact with the numbered CLI menu by typing an integer (1-7) to execute the various search, sort, and computation functions.

---

## Contribution
As I was the sole member of this project, I contributed to the whole of the project. This contribution is as follows:
* Implementation of Python logic and parallel lists
* Creation of search, filter, and computation algorithms
* Implementation of Selection Sort for chronological ordering
* CLI menu design, error handling, and user input validation
