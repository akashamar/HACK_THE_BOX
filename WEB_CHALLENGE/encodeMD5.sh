HOST=http://138.68.141.81:31608/

hash=$(curl -c 'cookie.txt' -s $HOST | head -n 6 | tail -n1 | cut -d '>' -f 4 | cut -d '<' -f1 | tr -d '\n' | md5sum | cut -d' ' -f1);

curl -s \
  -X POST \
  -b 'cookie.txt' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data "hash=$hash" \
  $HOST \
