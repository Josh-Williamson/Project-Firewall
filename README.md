Project Firewall
Overview:
developed by Josh Williamson and Xavier Spears. Project firewall is a fun tower defense game developed as our senior project at MNU.

Built Using:
Pygame http://pygametutorials.wikidot.com/start

Prerequisites:

    install Python 3.12
    install Pygame 2.5.2
    install IDE (Pycharm 2023.3.2 is preferred)
    install python and pycharm packages on your IDE to ensure it recognizes the syntax

Set up
1. Download contents of the main branch.
   
2. right-click on the ProjectFirewall folder and open folder in your IDE as a project.
   
3. add a new run/debug configuration to your the ProjectFirewall project.
   
       a. python

       b. make the script point to (where you saved the project to)\Project-FireWall\main_loop\main.py

       c. working directory the Project-Firewall folder

       d. hit apply and ok to add new configuration

        it should look similar to this:
![image](https://github.com/MNU-Fall-2023/Project-FireWall/assets/143554505/0332141a-ba76-4e06-b39a-844deb16203e)


Run application

    1. after completing the setup. hit your run/debug to get the application started and enjoy


Playing the Game

    Once you start the application, the game will start.
    Enemies will spawn at the beginning of the path (Orange Square) and will attack your base (Blue square).
    To place Tower to defend your base, you must select the number key that corresponds with the tower you want to place:
    
        1 = basic tower (mid speed shooting, 3 tile range)
        
        2 = advanced tower (slow shooting, 5 tile range)
        
        3 = rapid tower (rapid shooting, 5 tile range)
        
    Click on the tile you want to place your tower and your tower will spawn and shoot enemy sprites when they are in range.
    To place more tower you will need to reselect a tower type to place a new tower.
