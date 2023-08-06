package Validators;

import domain.User;

public class UserValidator extends RuntimeException {
    public static boolean isValidName(User u){
        return u.getName() != null && u.getName().length() <= 3 ;
    }

}
