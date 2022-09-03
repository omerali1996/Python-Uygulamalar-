# https://www.themoviedb.org website used for this demo.

import requests
import os

class theMoviedb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        
        self.api_key = "9a345b0668ac0be315c146be8613d1c6"

    def getPopulars(self,page):

        response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()
        
    def nowPlaying(self,page):
        response =requests.get(f"{self.api_url}movie/now_playing?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()

    def topRated(self,page):
        response = requests.get(f"{self.api_url}movie/top_rated?api_key={self.api_key}&language=en-US&page={page}")
        return response.json()

    def Search(self,keyword,page):
        response = requests.get(f"{self.api_url}search/movie?api_key={self.api_key}&language=en-US&query={keyword}&page={page}&include_adult=false")    
        return response.json()

 
movieApi = theMoviedb()

while True:
    print("menü".center(12,"*"))
    secim = input("1-Popular Filmler\n2-Vizyonda\n3-Top Rated\n4-Search Movie\n5-Çıkış\nSeçim: ")
    if secim =="5":
        break
    else:
        if secim=="1":
            page = int(input("page:"))
            movies = movieApi.getPopulars(page)
            list = []
            for movie in movies["results"]:
                print(movie["title"])
                list.append(movie["title"])
            # print(list)

        elif secim =="2":
            page = int(input("page:"))
            filmler = movieApi.nowPlaying(page)
            list = []
            for movie in filmler["results"]:
                print(movie["title"])
                list.append(movie["title"])
            # print(list)
        elif secim =="3":
            page = int(input("page:"))
            movies1 = movieApi.topRated(page)
            list =[]
            for movie in movies1["results"]:
                print(movie["title"])
                list.append(movie["title"])
            # print(list)
        elif secim=="4":
            keyword = input("film:").strip()
            page = int(input("page:"))
            movies2= movieApi.Search(keyword,page)
            list_title =[]
            list_overview =[]
            for movie in movies2["results"]:
                print(movie["title"])
                print("********")
                list_title.append(movie["title"])
            # print(list_title)
            for movie in movies2["results"]:
                print(movie["overview"])
                print("******")
                list_overview.append(movie["overview"])
            # print(list_overview)
    
        else:
            print("yanlış seçim !!!")

