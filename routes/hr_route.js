let express=require("express");
let router=express.Router();
let {users}=require('../models/users');
let {tasks}=require("../models/tasks");
router.get("/viewemployees",async (req,res)=>{
    // res.send("view employees router");
    let result=await users.find();
    res.send(result);
});

router.post("/assign-task",async (req,res)=>{
    let data=req.body;
    let newTask=new tasks(data);
    let result=await newTask.save();
    res.send(result);
});

router.put("/updatestatus",(req,res)=>{
    res.send("update status router");
});

router.delete("/deleteemployee/:id",async (req,res)=>{
    // res.send("delete employees router");
    let result=await users.findByIdAndDelete(req.params.id);
    if(result){
        res.send("emp deleted");
    }
    else{
        res.send("no user foundd");
    }

});

module.exports=router;

