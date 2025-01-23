def checkAgeCriteria (inputAge):
  if(inputAge):
    if(inputAge < 16):
      print('You are underage');
    elif(inputAge >= 60 and inputAge < 100):
      print('You are too old to have the license');
    elif(inputAge >= 18 and inputAge < 60):
      print('You are old enough to have the license');
    elif(inputAge >=16 and inputAge < 18):
      print('Wait till you reach 18.');
    else:
      print('May God bless your age but please sit at home and don\'t drive unless you were a hardcore biker');
  else:
    print('Please enter the age in Numbers');


inputAge = input('Please enter your age: ');

try:
  inputAge = int(inputAge);
  while(inputAge != 0):
    checkAgeCriteria(inputAge);
    inputAge = input('Please enter your age again: ');
    inputAge = int(inputAge);
  else:
    print(f'You entered {inputAge} command to exit the code.');
except ValueError:
  print(f'{inputAge} is not a NUMBER. What is your breed?');
