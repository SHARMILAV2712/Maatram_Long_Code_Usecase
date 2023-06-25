class User_details:
    print("Welcome to Tickety! Have a Good Day!")
    def __init__ (self,user_id, password,name,gender,mail):
        self.user_id=user_id
        self.password=password
        self.name=name
        self.gender=gender
        self.mail=mail
    def display_details(self):
        print("Name:",self.name,"\nGender:",self.gender,"\nMail ID:",self.mail,"\n-------------------")
    def logging_in(self,user_id_entered,password_entered):
        if self.user_id==user_id_entered and self.password==password_entered:
            print("Login Sucessful !\n-------------------")
            user1.display_details()
            t1.display_theatres()
            t2.display_theatres()
            t3.display_theatres()
            mv_list=int(input("Enter Theatre ID to see movie list:"))  
            if mv_list==2000:
                print("Movie listings at GALAXY THEATRE:","\n------------------")
                for movie_details in galaxy_movies:
                    movie = Movie_listings(*movie_details)
                    movie.display_movie()
                movie_select=input("Enter the movie ID to confirm:")
                if movie_select=="1g":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*200
                    print("Total ticket cost is:",amt)
                elif movie_select=="2g":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*150
                    print("Total ticket cost is:",amt)
                elif movie_select=="3g":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*150
                    print("Total ticket cost is:",amt)
                
            elif mv_list==2001:
                print("Movie listings at Alangar THEATRE:","\n------------------")
                for movie_details in alangar_movies:
                    movie = Movie_listings(*movie_details)
                    movie.display_movie()
                movie_select=input("Enter the movie ID to confirm:")
                if movie_select=="1a":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*150
                    print("Total ticket cost is:",amt)
                elif movie_select=="2a":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*200
                    print("Total ticket cost is:",amt)
                elif movie_select=="3a":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*200
                    print("Total ticket cost is:",amt)

            elif mv_list==2002:
                print("Movie listings at GALAXY THEATRE:","\n------------------")
                for movie_details in rohini_movies:
                    movie = Movie_listings(*movie_details)
                    movie.display_movie()
                movie_select=input("Enter the movie ID to confirm:")
                if movie_select=="1r":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*100
                    print("Total ticket cost is:",amt)
                elif movie_select=="2r":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*150
                    print("Total ticket cost is:",amt)
                elif movie_select=="3r":
                    seat_count=int(input("Enter no.of seats:"))
                    amt=seat_count*200
                    print("Total ticket cost is:",amt)

            else:
                print('none')
            
            conf=input("Enter 'yes' to confirm:")
            if conf=='yes':
                print("\n***************\nSuccessfully Booked\nThank you for using the app\n***************")
            else:
                print("Cancelled Booking")
        else:
            print("**Invalid Details**\n Please, Enter the details correctly")

class Theatre:
    def __init__(self,th_name,theatre_id,theatre_location,theatre_sp):
        self.theatre_id=theatre_id
        self.th_name=th_name
        self.theatre_location=theatre_location
        self.theatre_sp=theatre_sp
    def display_theatres(self):
        print("Theatre Name:",self.th_name,"\nTheater_ID:",self.theatre_id,"\nLocation:",self.theatre_location,"\nFeatures:",self.theatre_sp,"\n-------------------")
class Movie_listings:
    def __init__ (self,movie_id,movie_name,movie_lang,duration,certif,tick_cost):
        self.movie_id=movie_id
        self.movie_name=movie_name
        self.movie_lang=movie_lang
        self.duration=duration
        self.certif=certif
        self.tick_cost=tick_cost
    def display_movie(self):
        print("Movie ID:",self.movie_id,"\nMovie Name:",self.movie_name,"\nLanguage:",self.movie_lang,"\nDuration:",self.duration,"\nCertificate:",self.certif,"\nTicket Cost:",self.tick_cost,"\n-------------------")

user_id_entered = input("Enter user_id: ")
password_entered = input("Enter password: ")
user1 = User_details("sharmi27","9789","Sharmila","Female","sha@gmail.com")

t1=Theatre("GALAXY THEATRE",2000,"Vellore","\n4K quality with Dolby Atmos sound effect \nIt has maximum of 240 seats ")
t2=Theatre("Alangaar Cinemas",2001,"Arani","\nWide Screen with 3d sound quality\nIt has maximum of 200 seats ")
t3=Theatre("Rohini THEATRE",2002,"Chennai","\nIMAX Screen with 3d sound effect\nIt has maximum of 400 seats ")

galaxy_movies=[
     ["1g","PS2","Tamil",'2hrs 45mins',"U","Rs.200"],
     ["2g","Interstellar","English",'2hrs 40mins',"U","Rs.150"],
     ["3g","KFN","Tamil",'2hrs 10mins',"U","Rs.150"]
]
alangar_movies=[
     ["1a","KK","Tamil",'2hrs 30mins',"U","Rs.150"],
     ["2a","Mission to Mars","Hindi","3 hrs","U","Rs.200"],
     ["3a","Martian","English","2 hrs","U","Rs.200"]
]
rohini_movies=[
     ["1r","Sooriya Vamsam","Tamil","2 hrs 15 mins","U","Rs.100"],
     ["2r","Conjuring","English","2 hrs","A","Rs.150"],
     ["3r","MSD","Hindi","2 hrs","U","Rs.200"]
]
user1.logging_in(user_id_entered,password_entered)





