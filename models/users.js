let mongoose=require("mongoose");
let usersschema=mongoose.Schema({
    name:String,
    email:String,
    password:String,
    role:String

})

let users=mongoose.model('users',usersschema);
module.exports={users}

