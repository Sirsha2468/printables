function Menu(e) {
  let list = document.querySelector("ul");

  e.name === "grid-outline"
    ? ((e.name = "close"),
      list.classList.add("top-[80px]"),
      list.classList.add("opacity-100"))
    : ((e.name = "grid-outline"),
      list.classList.remove("top-[80px]"),
      list.classList.remove("opacity-100"));
}
