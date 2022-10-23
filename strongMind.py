ingredientList=['marinara', 'cheese', 'pepperoni', 'sausage']

myDict = {'cheese': ['marinara', 'cheese'], 'pepperoni': ['marinara','cheese', 'pepperoni'],\
		'sausage':['marinara', 'cheese', 'sausage']}

while True:

	userInput = input('press 1. for pizza maker\npress 2. for pizza chef\npress 3. to exit\n')

	if userInput == '1':

		while True:

			userInput2 = input("press 1. to see ingredients\npress 2. to add\npress 3. to delete ingredient\
			\npress 4. to update topping\npress 5. to go back\n")

			if userInput2=='1':
				print(ingredientList)

			elif userInput2=='2': #add nonexistant topping
				extraIng = input('add extra ingredient\n')
				if extraIng not in ingredientList:
					ingredientList.append(extraIng)
					print("item added")
				else:
					print("item already in ingredient list")

			elif userInput2=='3': #delete ingredient and update pizza list if pizza has said deleted ingredient
				deleteIng = input('Which ingredient would you like to delete (will remove from pizza ingredient list)?\n')
				if deleteIng in ingredientList:
					ingredientList.remove(deleteIng)
					for i in myDict.values():
						try:
							i.remove(deleteIng)
						except ValueError:
							pass
					print("item removed")
				else:
					print("not in ingredient list")

			elif userInput2=='4': #update topping and update the topping in pizza list as well
				updateIng = input('enter existing topping you would like to update:\n')
				if updateIng in ingredientList:
					itemIndex = ingredientList.index(updateIng)
					newIng = input('enter what you would like to update it with (will update pizza list too):\n')
					if newIng not in ingredientList:
						ingredientList[itemIndex] = newIng
						for i in myDict.values():
							try:
								i.remove(updateIng)
								i.append(newIng)
							except ValueError:
								pass
						print('item updated')
					else:
						print('already in ingredient list')
				else:
					print("topping not in list")

			elif userInput2=='5':
				break

			else:
				print('invalid input')

	elif userInput == '2': #pizza chef portion

		while True:

			userInput3 = input("press 1. to see pizza list\npress 2. to add pizzas\npress 3. to delete pizzas\
			\npress 4. to update topping\npress 5. update ingredients\npress 6. to go back\n")

			if userInput3=='1':
				for i in myDict.items():
					print(i)

			elif userInput3=='2': #add nonexistant pizza if ingredients are in ingredient list
				boo = False
				newZa = input('enter new pizza name\n')
				if newZa not in myDict: 
					x = list(map(str, input("Enter ingredients, seperate with space: ").split()))
					for i in x: #make sure ingredients are in list 
						if i not in ingredientList:
							boo = True
							break
					if boo==True:
						print('please update ingredient list before adding topping to pizza')
					else:
						myDict[newZa] = x
						print('pizza added')

				else:
					print("pizza already in list")

			elif userInput3=='3': #delete existing pizza
				deleteZa = input('Which pizza would you like to delete?\n')
				if deleteZa in myDict:
					del myDict[deleteZa]
					print("Pizza removed")
				else:
					print("not in pizza list")

			elif userInput3=='4': #update pizza
				updateZa = input('enter existing pizza you would like to update:\n')
				if updateZa in myDict:
					newZa = input('enter new pizza name\n')	
					if newZa not in myDict:
						myDict[newZa] = myDict.get(updateZa)
						del myDict[updateZa]
						print('pizza updated')
					else:
						print('pizza name already in list')			
				else:
					print("pizza not in list")

			elif userInput3=='5': #update pizza toppings as long as ingredients exist
				boo = False
				updateValues = input('enter pizza you would like to change the ingredients of\n')
				if updateValues in myDict:
					x = list(map(str, input("Enter ingredients, seperate with space: ").split()))
					for i in x:
						if i not in ingredientList:
							boo = True
							break
					if boo == True:
						print('at least one topping did not exist in ingredient list')
					else:
						myDict[updateValues] = x
						print('ingredients updated')
				else:
					print('pizza not in list')

			elif userInput3=='6':
				break

			else:
				print('invalid input')

	elif userInput =='3':
		break

	else:
		print('invalid input')

	print('------------------------')
 
print('exited')