require 'http'
require 'json'
require 'time'

file = File.read('data.json')
data_hash = JSON.parse(file)

while online = true
    response = HTTP.get("https://apiflask.alge1352.repl.co")

    data = JSON.parse response

    if response.code == 200
        puts "Data.json updated"
        data_hash = data
        File.write('data.json', JSON.dump(data_hash))
    else
        puts "API is not working. ERROR CODE: #{response.code}"
    end
    sleep 120
end
