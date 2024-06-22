package com.example.springBootRest.service;

import com.example.springBootRest.model.JobPost;
import com.example.springBootRest.repo.JobRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class JobService {
    @Autowired
    private JobRepo repo;

    public List<JobPost> getAllJobs(){
        return repo.getAllJobs();
    }
    public void addJobPost(JobPost post){
        repo.addJobPost(post);
    }

    public JobPost getJobPost(int postId) {
        return repo.getJobPost(postId);
    }

    public void updateJobPost(JobPost jobPost) {
        repo.updateJobPost(jobPost);
    }

    public void deleteJobPost(JobPost jobPost) {
        repo.deleteJobPost(jobPost);
    }
}
