function loadReact() {
    const domContainer = document.querySelector('.workshop-header');
    const root = ReactDOM.createRoot(domContainer);
    root.render(e(WorkshopHeader));
    debug.log("I actually got here....")
}
function loadGroups() {
    const domContainer = document.querySelector('#group-list');
    const root = ReactDom.CreateRoot(domContainer);
    root.render(e(Group))
    debug.log('got to loadGroups()')
}