#Zachary Breene
#Movies Program Project
#CSC110
#12/14/2020

def openFile():
  #Sampled from Lab 5
  rightFile = False
  while rightFile == False:
    filename = input("Enter file name: ")
    try:
      infile = open(filename, 'r')
      rightFile = True
    except IOError:
      print("File name not found, try again.")
    return infile

def getMovies():
  infile = openFile()
  titleList = []
  genreList = []
  runtimeList = []
  ratingList = []
  studioList = []
  releaseYearList = []
  line = infile.readline()
  line = line.strip()
  while line != '':
    title, genre, runtime, rating, studio, releaseYear = line.split(",")
    titleList.append(title)
    genreList.append(genre)
    runtimeList.append(runtime)
    ratingList.append(rating)
    studioList.append(studio)
    releaseYearList.append(releaseYear)
    line = infile.readline()
    line = line.strip()
  infile.close()

  return titleList, genreList, runtimeList, ratingList, studioList, releaseYearList

def findFilmsByStudio(studio, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList):
  studioFilmList = ''
  for i in range(len(titleList)):
    if studio == studioList[i]:
      studioFilmList = studioFilmList + titleList[i] + "," + genreList[i] + "," + runtimeList[i] + "," + ratingList[i] + "," + studioList[i] + "," + releaseYearList[i] + "\n"
  return studioFilmList

def longestFilmByGenre(genre, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList):
  runtime = 0
  for i in range(len(genreList)):
    if genreList[i] == genre and int(runtimeList[i]) > runtime:
      runtime = int(runtimeList[i])
  for i in range(len(genreList)):
    if int(runtimeList[i]) == runtime:
      longestFilm = titleList[i] + "," + genreList[i] + "," + runtimeList[i] + "," + ratingList[i] + "," + studioList[i] + "," + releaseYearList[i] + "\n" 
  return longestFilm

def findFilmsByRating(yearMin, yearMax, rating, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList):
  ratingFilmList = ''
  for i in range(len(ratingList)):
    if (releaseYearList[i] >= yearMin) and (releaseYearList[i] <= yearMax):
      if rating == ratingList[i]:
        ratingFilmList = ratingFilmList + titleList[i] + "," + genreList[i] + "," + runtimeList[i] + "," + ratingList[i] + "," + studioList[i] + "," + releaseYearList[i] + "\n"
  return ratingFilmList

def findFilmByTitle(title, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList):
  titleInfo = ''
  for i in range(len(titleList)):
    if title == titleList[i]:
      titleInfo = titleList[i] + "," + genreList[i] + "," + runtimeList[i] + "," + ratingList[i] + "," + studioList[i] + "," + releaseYearList[i] + "\n"
  return titleInfo

def avgFilmRuntimeByRating(rating, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList):
  runtimeAvg = 0
  summ = 0
  listForRuntimeAvg = []
  for i in range(len(ratingList)):
    if rating == ratingList[i]:
      summ = summ + int(runtimeList[i])
      listForRuntimeAvg.append(runtimeList[i])
  runtimeAvg = summ / len(listForRuntimeAvg)
  return runtimeAvg

def sortByYear(titleList, genreList, runtimeList, ratingList, studioList, releaseYearList):
  for i in range(0, len(releaseYearList)):
    earliestYear = i
    for j in range(i + 1, len(releaseYearList)):
      if releaseYearList[j] < releaseYearList[earliestYear]:
        earliestYear = j
    releaseYearList[i], releaseYearList[earliestYear] = releaseYearList[earliestYear], releaseYearList[i]
    titleList[i], titleList[earliestYear] = titleList[earliestYear], titleList[i]
    genreList[i], genreList[earliestYear] = genreList[earliestYear], genreList[i]
    runtimeList[i], runtimeList[earliestYear] = runtimeList[earliestYear], runtimeList[i]
    ratingList[i], ratingList[earliestYear] = ratingList[earliestYear], ratingList[i]
    studioList[i], studioList[earliestYear] = studioList[earliestYear], studioList[i]
  outfilename = input("Enter name of output file: ")
  outfile = open (outfilename, 'w')
  for i in range(len(releaseYearList)):
    outfile.write(titleList[i] + "," + genreList[i] + "," + runtimeList[i] + "," + ratingList[i] + "," + studioList[i] + "," + releaseYearList[i] + "\n")
  outfile.close()
  return

def getChoice():
    # Sampled from Lab 5
    print("")
    print("Make a selection from the following choices:")
    print("1 - Find all films produced by a certain studio")
    print("2 - Find the longest film of a specific genre")
    print("3 - Find all films made in a given year range with a specific rating")
    print("4 - Search for a film by title")
    print("5 - Find the average runtime of films with a certain rating")
    print("6 - Sort all lists by year and write the results to a new file")
    print("7 - Quit")
    OK = False
    while OK == False:
      try:
        choice = int(input("Enter your choice --> "))
        OK = True
      except ValueError:
        print("Not an integer, try again.")  
    print("")
    return choice

def main(): 
  #Sampled from Lab 5   
  titleList, genreList, runtimeList, ratingList, studioList, releaseYearList = getMovies()
  choice = getChoice()
  while choice != 7:
      if choice == 1:
          studio = input("Enter the studio: ")
          for i in range(len(studioList)):
            if studio not in studioList:
              print("Invalid choice - try again:")
              print('')
              studio = input("Enter the studio: ")
          studioFilmList = findFilmsByStudio(studio, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList)
          print(studio, " produced these films:")
          print('')
          print(studioFilmList)
          choice = getChoice()
      elif choice == 2:
          genre = input("Enter the genre: ")
          for i in range(len(genreList)):
            if genre not in genreList:
              print("Invalid choice - try again:")
              print('')
              genre = input("Enter the genre: ")
          longestFilm = longestFilmByGenre(genre, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList)
          print("The longest film with the genre ", genre, " is:")
          print('')
          print(longestFilm)
          choice = getChoice()
      elif choice == 3:
          yearMin = input("Enter the minimum year in the range: ")
          yearMax = input("Enter the maximum year in the range: ")
          for i in range(len(releaseYearList)):
            if yearMax < yearMin:
              print("Second year should be after first year - try again:")
              print('')
              yearMin = input("Enter the minimum year in the range: ")
              yearMax = input("Enter the maximum year in the range: ")
          rating = input("Enter the rating: ")
          for i in range(len(ratingList)):
            if rating not in ratingList:
              print("Invalid choice - try again:")
              print('')
              rating = input("Enter the rating: ")
          ratingFilmList = findFilmsByRating(yearMin, yearMax, rating, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList)
          print("The films made between ", yearMin, " and ", yearMax, " with a rating of ", rating, " are: ")
          print('')
          print(ratingFilmList)
          choice = getChoice()
      elif choice == 4:
          title = input("Enter the movie title: ")
          for i in range(len(titleList)):
            if title not in titleList:
              print("Invalid choice - try again:")
              print('')
              title = input("Enter the movie title: ")
          titleInfo = findFilmByTitle(title, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList)
          print("The movie and its information are: ")
          print('')
          print(titleInfo)
          choice = getChoice()
      elif choice == 5:
          rating = input("Enter the rating: ")
          for i in range(len(ratingList)):
            if rating not in ratingList:
              print("Invalid choice - try again:")
              print('')
              rating = input("Enter the rating: ")
          runtimeAvg = avgFilmRuntimeByRating(rating, titleList, genreList, runtimeList, ratingList, studioList, releaseYearList)
          print("The average runtime for films with a ", rating, " rating is ", runtimeAvg)
          choice = getChoice()
      elif choice == 6:
          sortByYear(titleList, genreList, runtimeList, ratingList, studioList, releaseYearList)
          choice = getChoice()
      else:
          print("Error in your choice")
          choice = getChoice()
  print("Good-bye")
    
main()
