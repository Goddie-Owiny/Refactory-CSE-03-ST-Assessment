const mongoose = require("mongoose");
//Access the schema in mongoose function 
// const schema = mongoose.schema;

const studentSchema = new mongoose.Schema({
  name:{
    type:String,
    trim:true
  },

  fullname:{
    type:String,
    trim:true
  },

  courseoutline:{
    type:String,
    trim:true
  },

  entry:{
    type:String,
    trim:true
  },

  take:{
    type:String,
    trim:true
  },

  gender:{
    type:String,
    trim:true
  },

  date:{
    type:String,
    trim:true
  },

  place:{
    type:String,
    trim:true
  },

  box:{
    type:String,
    trim:true
  }

});

module.exports = mongoose.model("student", studentSchema)