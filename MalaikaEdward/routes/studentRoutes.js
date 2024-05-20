const express = require('express');
const router = express.Router();

const student = require("../models/student")

router.get("/register", (req, res) =>{
    res.render("studentregister");
});

//post route
router.post("/register", async (req, res) => {
    try {
      const student = new student(req.body);
      console.log(student);
      await student.save();
      res.redirect("/register");
    } catch (error) {
      // incase of errors
      res.status(400).send("sorry something went wrong");
      console.log("Error +registering the baby..", error);
    }
  });



module.exports = router;