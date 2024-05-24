function getMAC() {
    try {
        const network = new ActiveXObject('WScript.Network');
        const MACAddress = network.ComputerName + ' : ' + network.UserDomain + ' : ' + network.MACAddress;
        console.log(MACAddress);
    } catch (e) {
        console.log(e);
    }
}


getMAC()