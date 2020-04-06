set -e

docker-compose down --remove-orphans
sleep 5
echo '# start everything'
docker-compose up -d
echo '# wait for things to settle down ...'
sleep 10
echo '# logs'
docker-compose logs -f
