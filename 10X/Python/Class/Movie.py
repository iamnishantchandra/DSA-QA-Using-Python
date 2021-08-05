'''
Print Movie Description -- Classes Practice Problems
Write a Movie class for which you can create movie objects. The objects should have the following 
variables: integer length_in_minutes, integer num_characters, string language. Each object should also 
have a run method which prints out: "This is a movie with characters and is minutes long."

Input
First line is a string, denoting the language of the movie Second line is an integer, denoting the number 
of characters Third line is an integer, denoting the length in minutes

Output
The output should be the return statement of run: "This is a movie with characters and is minutes long."

Example
Input:

French
4
200
Output:

This is a French movie with 4 characters and is 200 minutes long.
First line is French indicating the movie's language is French Second line is 4, indicating that the 
movie has 4 characters Third line is 200, indicating that the movie is 200 minutes long
'''
class Movie:
    def __init__(self,lang,cha,mint):
            self.lang=lang
            self.cha=cha
            self.mint=mint
    def run(self):
        s="This is a "+self.lang+" movie with "+str(self.cha) +" characters and is "+str(self.mint)+" minutes long."
        return s

if __name__ == "__main__":
    MovObj = Movie(input(), input(),input())
    print(MovObj.run())
