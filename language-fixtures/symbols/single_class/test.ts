export class UserService {
    private db: Database;
    
    constructor(db: Database) {
        this.db = db;
    }
}
