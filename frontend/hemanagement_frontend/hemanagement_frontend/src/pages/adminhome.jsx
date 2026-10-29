function AdminHome() {
    let currentuser=JSON.parse(localStorage.getItem("currentuser"));
    return (
        <div>
            <h1>welcome {currentuser.name}</h1>

        </div>)
}
export default AdminHome