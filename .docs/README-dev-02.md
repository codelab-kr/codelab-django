docker pull rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

http://localhost:15672/
guest / guest


celery -A services.shop.shop worker -l info
http://localhost:15672/
guest / guest



celery -A services.shop.shop flower
http://localhost:5555/

