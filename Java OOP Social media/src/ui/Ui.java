package ui;

import domain.Friendship;
import domain.User;
import service.ServiceFriendship;
import service.ServiceUser;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class Ui {
    private final ServiceFriendship srvFr;
    private final ServiceUser srvUsr;

    public Ui(ServiceFriendship srvFr, ServiceUser srvUsr) {
        this.srvFr = srvFr;
        this.srvUsr = srvUsr;
    }

    public void Starting(){
        srvUsr.add(1,"Iuga", "Daniel", "danieliuga33@yahoo.com", "Iuga");
        srvUsr.add(2,"Chis", "Marcus", "marcuschis@yahoo.com", "Marcus");
        srvUsr.add(3,"Urian", "Rares", "tee@yahoo.com", "Tee");
        srvUsr.add(4,"Ferdean", "Calin", "fefe@yahoo.com", "fefe");
        srvUsr.add(5,"Hurubean", "Alexia", "lexi@yahoo.com", "fefe");
        srvUsr.add(6,"Horoi", "Sile", "silecamataru@yahoo.com", "fefe");
        List<Integer> list = new ArrayList<>();
        list.add(2); list.add(3); list.add(4);list.add(6);
        srvFr.add(1,list);
        List<Integer> newList = new ArrayList<>();
        newList.add(2); newList.add(1);
        srvFr.add(6,newList);
    }

    /** ---------PRINT MENUS--------**/
    public static void printMainMenu(){
        System.out.println("            Welcome");
        System.out.println(" |    (1) User Menu        |");
        System.out.println(" |    (2) Friendship Menu  |");
        System.out.println(" |    (x) Exit the app     |");
    }

    public static void userMenu(){

        System.out.println(" |   (1) ADD User        |");
        System.out.println(" |   (2) DELETE User     |");
        System.out.println(" |   (a) Show all Users  |");
        System.out.println(" |   (x) Exit User Menu  |");
    }

    public static void friendshipMenu(){

        System.out.println("|   (1) ADD Friendship       |");
        System.out.println("|   (2) DELETE Friendship    |");
        System.out.println("|   (2.1) DELETE friends     |");
        System.out.println("|  from a Friendship         |");
        System.out.println("|   (a) Show all Friendships |");
        System.out.println("|   (x) Exit Friendship Menu |");

    }

    public static <E> void showAll(List<E> elems){
        System.out.println();
        if (elems.size() == 0){
            System.out.println("There is nothing to show !\n");
            return;
        }
        elems.forEach(System.out::println);
        System.out.println();
    }
    /* -----------------------------**/

    /** -------User Operations-------**/
    void addUser(Scanner sc){
        int id;
        if (srvUsr.size() == 0)
             id = 1;
        else id = srvUsr.getRepo().getRepo().get(srvUsr.size() - 1).getId() + 1;
        System.out.print("Name: ");
        String n = sc.nextLine();
        System.out.print("Surname: ");
        String sn = sc.nextLine();
        System.out.print("email: ");
        String e = sc.nextLine();
        System.out.print("password: ");
        String p = sc.nextLine();
        srvUsr.add(id, n, sn, e, p);
    }
    void delUser(Scanner sc){
        if (srvUsr.size() == 0){
            System.out.println("There are no Users !!!");
            System.out.println(" ");
            return;
        }
        showAll(srvUsr.getAll());
        System.out.print("Give the id of the User you want to delete: ");
        int id = sc.nextInt();
        if (srvUsr.exist(id)) {
            srvUsr.remove(id);
            deleteInCascade(id);
            System.out.println("The User was successfully removed !\n");
        }
        else System.out.println("There is no User with this id !");
    }

    /* -----------------------------**/

    /** ----Friendship Operations----**/
    void addFriendship(Scanner sc){
        if (srvUsr.size() < 2){
            if (srvUsr.size() == 0) {
                System.out.println("There are no Users !!!");
                System.out.println(" ");
                return;
            }
            System.out.println("There are not enough users to make a friendship !!");
            return;
        }
        showAll(srvUsr.getAll());
        System.out.print("Give the id of the User you want to add friends: ");
        int idFr = sc.nextInt();
        if(!srvUsr.exist(idFr)){
            System.out.println("This User does not exist !!!");
            System.out.println(" ");
            return;
        }
        if(srvFr.exist(idFr)){
            System.out.println("This User does already have friends !");
            System.out.println("Do you want to add more?!");
            System.out.println("[1]. Yes");
            System.out.println("[2]. No");
            int choice = sc.nextInt();
            if (choice == 1){
                Friendship fr = srvFr.getRepo().findById(idFr);
                List<Integer> notFriends = notFriendWith(fr);
                System.out.println("The Users that are not your friends are: ");
                for(int i = 0; i < notFriends.size(); i++)
                    System.out.println((i+1) + ". " + srvUsr.getRepo().findById(notFriends.get(i)));
                fr = addFriends(sc,notFriends,fr);
                if (Objects.equals(fr, new Friendship()))
                    return;
                System.out.println("The new friends were added successfully !");
            }
        }else{
           Friendship fr = new Friendship(idFr, new ArrayList<>());
            List<Integer> notFriends = notFriendWith(fr);
            System.out.println("The available Users are: ");
            for(int i = 0; i < notFriends.size(); i++)
                System.out.println((i+1) + ". " + srvUsr.getRepo().findById(notFriends.get(i)));
            fr = addFriends(sc,notFriends,fr);
            if (Objects.equals(fr, new Friendship()))
                return;
            srvFr.add(idFr,fr.getFriends());
            System.out.println("The new friends were added successfully !");
        }

    }

    Friendship addFriends(Scanner sc, List<Integer> notFriends, Friendship fr){
        System.out.print("Choose how many friends you want to add: ");
        int n = sc.nextInt();
        if (n > notFriends.size()){
            System.out.println("There are not enough users !!!");
            return new Friendship();
        }
        for(int idNotFriends:notFriends)
            System.out.println("ID: " + idNotFriends  +" User: " + srvUsr.getRepo().findById(idNotFriends).getSurname()
                    + " " + srvUsr.getRepo().findById(idNotFriends).getName());
        for (int i = 0; i < n; i++){
            if (i == 0) System.out.print("Give the id of the first user you want to add: ");
            if (i == 1) System.out.print("Give the id of the second user you want to add: ");
            if (i == 2) System.out.print("Give the id of the third you want to add: ");
            if (i >= 3) System.out.print("Give the id of the "+ (i+1) +"th you want to add: ");
            int ids = sc.nextInt();
            if (notInList(ids, notFriends)) {
                User u = srvUsr.getRepo().findById(ids);
                if (u.getId() == 0)
                    System.out.println("The User with " + ids + " doesn't exist !!");
            } else fr.addFriend(ids);
        }
        return fr;
    }



    void delFriendship(Scanner sc){
        if (srvFr.size() == 0){
            System.out.println("There is no friendship to delete");
            return;
        }
        showAll(srvFr.getAll());
        System.out.print("Choose the id of the friendship you want to delete: ");
        int id = sc.nextInt();
        if (!srvFr.exist(id)){
            if (!srvUsr.exist(id))
                System.out.println("This User doesn't exist !!");
            else System.out.println("This user does not have a friendship yet");
            return;
        }
        srvFr.remove(id);
        System.out.println("The friendship was successfully removed!!");
    }


    void delFriends(Scanner sc){
        if (srvFr.size() == 0){
            System.out.println("There is no friendship to delete it's friends");
            return;
        }
        System.out.println();
        showAll(srvFr.getAll());
        System.out.println();
        System.out.print("Choose the id of the friendship you want to delete: ");
        int id = sc.nextInt();
        if (!srvFr.exist(id)){
            if (!srvUsr.exist(id))
                System.out.println("This User doesn't exist !!");
            else System.out.println("This user does not have a friendship yet");
            return;
        }
        Friendship fr = srvFr.getRepo().findById(id);
        User user = srvUsr.getRepo().findById(id);
        System.out.println("The " + user.getSurname() + "'s friends are: ");
        for(int i = 0; i < fr.getFriends().size(); i++)
            System.out.println((i+1) + ". " + srvUsr.getRepo().findById(fr.getFriends().get(i)));
        System.out.print("Choose how many you want to delete: ");
        int n = sc.nextInt();
        if (n > fr.getFriends().size()){
            System.out.println("There are not enough friends to delete !!!");
            return;
        }
        System.out.println();
        for(int idFriends:fr.getFriends())
            System.out.println("ID: " + idFriends  +" User: " + srvUsr.getRepo().findById(idFriends).getSurname() +
                    " " + srvUsr.getRepo().findById(idFriends).getName());
        System.out.println();
        for(int i = 0; i < n; i++){
            if (i == 0) System.out.print("Give the id of the first user you want to delete: ");
            if (i == 1) System.out.print("Give the id of the second user you want to delete: ");
            if (i == 2) System.out.print("Give the id of the third you want to delete: ");
            if (i >= 3) System.out.print("Give the id of the " + (i+1) + "th user you want to delete: ");
            int idToDel = sc.nextInt();
            if (notInList(idToDel, fr.getFriends()) | !srvUsr.exist(idToDel)){
                if (!srvUsr.exist(idToDel) && notInList(idToDel, fr.getFriends()))
                    System.out.println("This user does not exist !!!");
                else System.out.println("This User is not in " + user.getSurname() + "'s friend list !!!");
            } else fr.removeFriend(idToDel);
        }
        if (fr.getFriends().size() == 0) srvFr.remove(fr.getId());
        System.out.println("\nThe Users were successfully deleted from " + srvUsr.getRepo().findById(id).getSurname() +
                "'s friend list !\n");
    }

    /* -----------------------------**/

    /** ------------UTILS-----------**/

    public static boolean notInList(int id, List<Integer> list){
        for(int ids:list)
            if (ids == id)
                return false;
        return true;
    }

    List<Integer> notFriendWith(Friendship fr){
        List<Integer> rez = new ArrayList<>();
        List<Integer> friends = fr.getFriends();
        if (Objects.equals(friends, new ArrayList<Integer>())) {
            for (User usr : srvUsr.getAll())
                if (usr.getId() != fr.getId())
                    rez.add(usr.getId());
            return rez;
        }
        else {
            for (User usr : srvUsr.getAll())
                if (notInList(usr.getId(), friends) && usr.getId() != fr.getId()) {
                    rez.add(usr.getId());
                }
        }
        return rez;
    }

    public void deleteInCascade(int id){
        for (Friendship fr: srvFr.getAll()){
            if (!notInList(id, fr.getFriends())) {
                fr.removeFriend(id);
            }
        }
        for (Friendship fr: srvFr.getAll()){
            if (fr.getId() == id) {
                srvFr.remove(fr.getId());
                return;
            }
        }

    }

    /** -----------------------------**/

    public void run(){
        Starting();
        Scanner sc = new Scanner(System.in);
        label:
        while (true){
            printMainMenu();
            System.out.print("Give your option: ");
            String option = sc.nextLine();
            switch (option) {
                case "1":
                    label1:
                    while (true) {
                        userMenu();
                        System.out.print("Give your option: ");
                        String option1 = sc.nextLine();
                        while (option1.length() < 1)
                            option1 = sc.nextLine();
                        switch (option1) {
                            case "1":
                                addUser(sc);
                                break;
                            case "2":
                                delUser(sc);
                                break;
                            case "a":
                                showAll(srvUsr.getAll());
                                break;
                            case "x":
                                break label1;
                            default:
                                System.out.println("Wrong Option ! Try again !");
                                break;
                        }
                    }
                    break;
                case "2":
                    label2:
                    while (true) {
                        friendshipMenu();
                        System.out.print("Give your option: ");
                        String option2 = sc.nextLine();
                        while (option2.length() < 1)
                            option2 = sc.nextLine();
                        switch (option2) {
                            case "1":
                                addFriendship(sc);
                                break;
                            case "2":
                                delFriendship(sc);
                                break;
                            case "2.1":
                                delFriends(sc);
                                break;
                            case "a":
                                showAll(srvFr.getAll());
                                break;
                            case "x":
                                break label2;
                            default:
                                System.out.println("Wrong Option ! Try again !");
                                break;
                        }
                    }
                    break;
                case "x":
                    break label;
                default:
                    System.out.println("Wrong Option ! Try again !");
                    break;
            }
        }
    }
}
