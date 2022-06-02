var months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];


// Creates a new date

function createDate() {
    date = new Date();
    var d = date.getDate();
    var m = date.toLocaleString("default", {
        month: "long"
    })
    var y = date.getFullYear();
    return m + ' ' + d + ',' + ' ' + y
}

//Creates the date from server formatted as a new date

function createDateFromServer(date) {
    monthInNumber = date.substring(5, 7) - 1;
    var y = date.substring(0, 4);
    var m = months[monthInNumber];
    var d = date.substring(8);
    return m + ' ' + d + ',' + ' ' + y
}