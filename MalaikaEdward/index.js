const express = require('express');
const mongoose =require("mongoose")
const path =require("path");
const cors = require("cors");
const passport = require("passport")
const expressSession = require("express-session")({
  secret:"secret",
  resave:false,
  saveUninitialized:false
})

require("dotenv").config();

//importing routes
const studentRoutes = require("./routes/studentRoutes");


// instantiations
const app = express();

//Configurations
mongoose.connect(process.env.DATABASE,{
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

mongoose.connection
  .once("open", () => {
    console.log("Mongoose connection open");
  })
  .on("error", err => {
    console.error(`Connection error: ${err.message}`);
 });





app.set("view engine","pug"); // setting the view engine to pug
app.set("views", path.join(__dirname,"views")); //specify the directory where the views are found

// Middleware
app.use(express.static(path.join(__dirname, "public")))//set directory fot static fires 
app.use(express.urlencoded({extended:true}));
app.use(express.json());
app.use(cors());



//Express session configurations 
app.use(expressSession);
app.use(passport.initialize());
app.use(passport.session());

// //passport configuration
// passport.use(Administer.createStrategy());
// passport.serializeUser(Administer.serializeUser());
// passport.deserializeUser(Administer.deserializeUser());


//use imported routes
app.use("/", studentRoutes);













// Always the last line in your code
app.listen(3000, () => console.log('listening on port 3000'));
