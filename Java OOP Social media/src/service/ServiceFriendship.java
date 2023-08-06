package service;

import domain.Friendship;
import domain.User;
import repository.RepoFriendship;

import java.util.List;

public class ServiceFriendship {
    private RepoFriendship repo;

    public ServiceFriendship(RepoFriendship repo) {
        this.repo = repo;
    }

    public void add(int id, List<Integer> f){
        Friendship fr = new Friendship(id, f);
        repo.add(fr);
    }

    public void remove(int id){
        Friendship f = repo.findById(id);
        repo.remove(f);
    }

    public void addFriend(int idFriendship, int id){
        if (repo.exist(idFriendship))
            if (!repo.isFriendWith(idFriendship, id)){
                Friendship fr = repo.findById(idFriendship);
                fr.addFriend(id);
            }
    }

    public void delFriend(int idFriendship, int id){
        if (repo.exist(idFriendship))
            if (!repo.isFriendWith(idFriendship, id)){
                Friendship fr = repo.findById(idFriendship);
                fr.removeFriend(id);
            }
    }
    public boolean exist(int id){return repo.exist(id);}
    public List<Friendship> getAll(){return repo.getRepo();}
    public RepoFriendship getRepo(){return this.repo;}
    public int size(){return repo.size();}
}
