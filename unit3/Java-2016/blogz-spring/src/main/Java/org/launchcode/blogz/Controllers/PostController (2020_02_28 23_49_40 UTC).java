package org.launchcode.blogz.controllers;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.launchcode.blogz.models.Post;
import org.launchcode.blogz.models.User;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class PostController extends AbstractController {

	private List<Post> posts;

	@RequestMapping(value = "/blog/newpost", method = RequestMethod.GET)
	public String newPostForm() {
		return "newpost";
	}
	
	@RequestMapping(value = "/blog/newpost", method = RequestMethod.POST)
	public String newPost(HttpServletRequest request, Model model) {
		
		// implement newPost
		try {
		String title = request.getParameter("title");
		String body = request.getParameter("body");
		} catch (DataIntegrityViolationException e) {
			String error = "Post is too long.";
			model.addAttribute("error", error);
			return "newpost";
		}
		
		String title = request.getParameter("title");
		String body = request.getParameter("body");
		
		if(title == "" || title == null || body == "" || body == null) {
			String error = "One or more fields are empty";
			model.addAttribute("value", title);
			model.addAttribute("body", body);
			model.addAttribute("error", error);
			return "newpost";
		}
		
		
		HttpSession s = request.getSession();
		User u = getUserFromSession(s);
		Post p = new Post(title,body,u);
		postDao.save(p);
		int uid = p.getUid();
		String username = u.getUsername();
		
		
		return String.format("redirect:blog%s/%s/", username, uid); // this redirect should go to the new post's page  		
	}
	
	@RequestMapping(value = "/blog/{username}/{uid}", method = RequestMethod.GET)
	public String singlePost(@PathVariable String username, @PathVariable int uid, Model model) {
		
		// implement singlePost
		Post p = postDao.findByUid(uid);
		String title = p.getTitle();
		String body = p.getBody();
		model.addAttribute("title", title);
		model.addAttribute("body", body);
		model.addAttribute("username", username);
		model.addAttribute("post", p);
		return "post";
	}
	
	@RequestMapping(value = "/blog/{username}", method = RequestMethod.GET)
	public String userPosts(@PathVariable String username, Model model) {
		
		//implement userPosts
		User u = userDao.findByUsername(username);
		List <Post> posts = u.getPosts();
		model.addAttribute("posts", posts);
		
		return "blog";
	}
	
}
