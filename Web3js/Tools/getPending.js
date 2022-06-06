var Web3 = require('web3');
const node = new Web3.providers.HttpProvider("https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0");
var web3 = new Web3(node);

// web3.eth.getPendingTransactions().then(console.log);

// console.log(web3.isConnected());
// web3.eth.getPendingTransactions().then(console.log);

// web3.eth.filter("pending").watch(
//     function(error,result){
//         if (!error) {
//             console.log(result);
//         }
//     }
// )


// if (typeof web3 !== 'undefined') {
//     web3 = new Web3(web3.currentProvider);
// } else {
//     // set the provider you want from Web3.providers
//     web3 = new Web3(new Web3.providers.HttpProvider("https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"));
// }

// web3.eth.getBlock(48, function(error, result){
//     if(!error)
//         console.log(result)
//     else
//         console.error(error);
// })

// web3.eth.getPendingTransactions().then(console.log);

// var subscription = web3.eth.subscribe('PendingTransactions', function(error, result){})
// .on("data", function(transaction){
//     console.log(transaction);
//     web3.eth.getTransaction(transaction).then(response => console.log(`${transaction}: ${JSON.stringify(response)}`));
// });

// subscription = web3.eth.subscribe('pendingTransactions', function (error, result) {})
//     .on("data", function (transactionHash) {
//         web3.eth.getTransaction(transactionHash)
//         .then(function (transaction) {
//             createNode(transaction.from, transaction.to);
//         });
//     })

var subscription = web3.eth.subscribe('pendingTransactions', function (error, result)
{
    if (!error)
        console.log(result);
})
    .on("data", function (transaction)
    {
        console.log(transaction);
    });