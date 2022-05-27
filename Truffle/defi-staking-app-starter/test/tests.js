class Test {
  constructor() {
    this.name = "Javascript Tests";
  }

  normal() {
    console.log(this.name);
  }

  arrow() {
    let n = () => this.name;
    console.log(n());
  }
}

let t1 = new Test();
t1.normal();
t1.arrow();
