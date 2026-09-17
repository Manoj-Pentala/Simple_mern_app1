let express=require("express");
let app=express();
// app.get("/getstudent",(req,res)=>{
//     res.send("get students are called");
// });
// app.post("/addstudent",(req,res)=>{
//     res.send("add student called");
// });

// app.put("/updatestudent",(req,res)=>{
//     res.send("student updated");
// })

// app.delete("/deletestudent",(req,res)=>{
//     res.send("student deleted");
// })



let hrroutes=require("./routes/hr_route");
let emprouter=require("./routes/emp_route");
let mongoose=require("mongoose");
mongoose.connect("mongodb://localhost:27017/hrmanagement")
.then(()=>{
    console.log("connected to mongodb");
}).catch((err)=>{
    console.log(err);
})

app.use(express.json());

app.use("/api/hr",hrroutes);
app.use("/api/emp",emprouter);

app.listen(3000,()=>{
    console.log("server listening to poet number 3000");
})


