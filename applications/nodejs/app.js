const express = require('express')
const axios = require('axios');
const app = express()
const port = process.env.LISTENPORT
const url = process.env.ROOTAPIURL
const apikey = process.env.APIKEY
const apitoken = process.env.APITOKEN

app.use(express.static(__dirname + '/public'));

// list all the system packages I have access to
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

// go get the metadata on a system package
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

// list out all your checklists and their relevant scores
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

// POAM Risk Cube Numbers -- realize you have to have a POAM for any of this to come back correctly.
app.get('/api/systempackage/:systemKey/riskcube/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json"
        }
    }
    var systemKey = req.params.systemKey;
    var urlRequest = url + '/systempackage/' + systemKey + '/poamcube/?applicationKey=' + apikey
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

// Compliance Records -- realize you have to generate a save a compliance for this to return any data
app.get('/api/systempackage/:systemKey/compliance/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json"
        }
    }
    var systemKey = req.params.systemKey;
    var urlRequest = url + '/systempackage/' + systemKey + '/compliance/?applicationKey=' + apikey
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

// Template Records -- you can pass in the template type and optional search string
app.get('/api/templates/:templateType/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json"
        }
    }
    var templateType = req.params.templateType;
    let searchString = req.query.search;
    
    var urlRequest = url + '/templates/' + templateType + '/?applicationKey=' + apikey + '&searchString=' + searchString;
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

// Hardware/Device Records 
app.get('/api/systempackage/:systemKey/hardware/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    }
    var systemKey = req.params.systemKey;
    var urlRequest = url + '/systempackage/' + systemKey + '/hardware/?applicationKey=' + apikey
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

// Software Records 
app.get('/api/systempackage/:systemKey/software/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    }
    var systemKey = req.params.systemKey;
    var urlRequest = url + '/systempackage/' + systemKey + '/software/?applicationKey=' + apikey
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

// Ports/Protocols/Services Records 
app.get('/api/systempackage/:systemKey/ppsm/', function (req, res) {
    const config = {
        method: 'get',
        headers: {            
            "Authorization": "Bearer " + apitoken,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    }
    var systemKey = req.params.systemKey;
    var urlRequest = url + '/systempackage/' + systemKey + '/ppsm/?applicationKey=' + apikey
    console.log('Calling ' + urlRequest)
    axios.get(urlRequest, config).then(resp => {
        res.send(resp.data)
    });
});

var server = app.listen(port, function () {
    console.log('Node server is running on port ' + port + '...')
});