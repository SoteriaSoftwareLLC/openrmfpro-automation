const express = require('express')
const axios = require('axios');
const app = express()
const port = process.env.LISTENPORT
const url = process.env.ROOTAPIURL
const apikey = process.env.APIKEY
const apitoken = process.env.APITOKEN

// const formData = {
//     applicationKey: apikey
// };

app.use(express.static(__dirname + '/public'));

app.get('/api/systempackages/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json"
        }
    }
    console.log('Calling ' + url + '/systempackages/?applicationKey=' + apikey)
    axios.get(url + '/systempackages/?applicationKey=' + apikey, config).then(resp => {
        res.send(resp.data)
    });
});

app.get('/api/systempackage/:systemKey/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json"
        }
    }
    var systemKey = req.params.systemKey;
    var urlRequest = url + '/systempackage/' + systemKey + '/?applicationKey=' + apikey
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

app.get('/api/systempackage/:systemKey/checklists/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json"
        }
    }
    var systemKey = req.params.systemKey;
    var urlRequest = url + '/systempackage/' + systemKey + '/checklists/?applicationKey=' + apikey
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

var server = app.listen(port, function () {
    console.log('Node server is running on port ' + port + '...')
});