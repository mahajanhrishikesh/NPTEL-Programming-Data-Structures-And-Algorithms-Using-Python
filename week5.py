from datetime import datetime
books = dict()
current_book = input()
while current_book!='Borrowers':
  current_book = input()
  if current_book == 'Borrowers':
    break
  current_book_category = current_book[:3]
  #current_book_category_index = current_book[4:7]
  current_book_name = current_book[8:]
  books[current_book_category] = current_book_name

borrowers = dict()
current_borrower = current_book
while current_borrower != 'Checkouts':
  current_borrower = input()
  if current_borrower == 'Checkouts':
    break
  current_borrower_id = current_borrower[:7]
  current_borrower_name = current_borrower[8:]
  borrowers[current_borrower_id] = current_borrower_name
  
records = []
current_record = current_borrower
while current_record != 'EndOfInput':
  current_record = input()
  if current_record == 'EndOfInput':
    break
  record_borrower_id = current_record[:7]
  record_book_category = current_record[8:11]
  record_book_category_id = current_record[8:15]
  record_date = current_record[16:]
  final_text = record_date+'~'+borrowers[record_borrower_id]+'~'+record_book_category_id+'~'+books[record_book_category]
  records.append(final_text)

records.sort(key= lambda date: (datetime.strptime(date[:10], "%Y-%m-%d"), date.split('~')[1], date.split('~')[2], date.split('~')[3]))

for i in records:
  print(i)