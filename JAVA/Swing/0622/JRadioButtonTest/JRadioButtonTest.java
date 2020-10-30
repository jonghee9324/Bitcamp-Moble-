import java.awt.Container;
import java.awt.FlowLayout;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JRadioButton;

public class JRadioButtonTest extends JFrame {
	
	public JRadioButtonTest() {
		setTitle("라디오버튼 만들기  예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(new FlowLayout());

		ButtonGroup g = new ButtonGroup();  // 버튼 그룹 객체 생성
		
		// 라디오버튼 2개 생성
		JRadioButton rb1 = new JRadioButton("자바");
		JRadioButton rb2 = new JRadioButton("C언어", true);
		
		// 버튼 그룹에 3개의 라디오버튼 삽입
		g.add(rb1);
		g.add(rb2);

		// 컨텐트팬에 3 개의 라디오버튼 삽입
		c.add(rb1); c.add(rb2); 

		setSize(250,150);
		setVisible(true);
		
	}
	
	public static void main(String[] args) {
		new JRadioButtonTest();
	}

}
