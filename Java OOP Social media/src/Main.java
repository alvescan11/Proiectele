import repository.RepoFriendship;
import repository.RepoUser;
import service.ServiceFriendship;
import service.ServiceUser;
import Validators.UserValidator;
import ui.Ui;

public class Main {

    public static void main(String[] args) {
        RepoUser repoUsr = new RepoUser();
        UserValidator validator = new UserValidator();
        ServiceUser usr = new ServiceUser(repoUsr,validator);
        RepoFriendship repoFr= new RepoFriendship();
        ServiceFriendship fr = new ServiceFriendship(repoFr);
        Ui ui = new Ui(fr, usr);

        ui.run();
    }
}