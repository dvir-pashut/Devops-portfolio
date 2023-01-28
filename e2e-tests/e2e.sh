#!/bin/bash
#sleep 10

#testing the main funcuins 
curl -I localhost
curl -I localhost/avliable-books
curl -I localhost/contact

curl -o /dev/null -w "%{http_code}"  curl -X POST -d "name=some_name&email=example%40email.com&message=importantstuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuf" http://localhost/contact 

for i in {1..100}; do
  curl -o /dev/null -w "%{http_code}" curl -X POST -d "book-name=Book$i&Author-name=Author$i&summery=A+novel+about+the+decadence+and+excess+of+the+Roaring+Twenties&rating=$((i))&email=example%40email.com&submit=" http://localhost/insert-book
done


