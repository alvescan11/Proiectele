package service;
import Validators.UserValidator;
import domain.User;
import repository.RepoUser;


import java.util.List;

public class ServiceUser {
    private RepoUser repo;
    private UserValidator validator;
    public ServiceUser(RepoUser repo, UserValidator validator) {
        this.repo = repo;
    }


    public  void add(int id, String name, String surname, String email, String password ){
        User user = new User(id, name, surname, email,password);
        if(validator.isValidName(user)){
            repo.add(user);
        }
    }

    public void remove(int id){
        User u = repo.findById(id);
        repo.remove(u);
    }
    public List<User> getAll(){return repo.getRepo();}
    public boolean exist(int id){return repo.exist(id);}
    public RepoUser getRepo(){return this.repo;}
    public int size(){return repo.size();}

}