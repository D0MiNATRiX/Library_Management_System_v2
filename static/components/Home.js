import AdminHome from "./AdminHome.js"
import LibrarianHome from "./LibrarianHome.js"
import StudentHome from "./StudentHome.js"

export default{
    template: `
    <div>
        <AdminHome v-if="userRole=='admin'" />
        <LibrarianHome v-if="userRole=='librarian'" />
        <StudentHome v-if="userRole=='student'" />
    </div>
    `,
    data() {
        return {
            userRole: localStorage.getItem('role')
        }
    },
    components: {
        AdminHome,
        LibrarianHome,
        StudentHome
    },
}