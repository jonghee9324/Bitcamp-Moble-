import java.awt.Container;
import java.awt.FlowLayout;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JRadioButton;

public class JRadioButtonTest extends JFrame {
	
	public JRadioButtonTest() {
		setTitle("������ư �����  ����");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(new FlowLayout());

		ButtonGroup g = new ButtonGroup();  // ��ư �׷� ��ü ����
		
		// ������ư 2�� ����
		JRadioButton rb1 = new JRadioButton("�ڹ�");
		JRadioButton rb2 = new JRadioButton("C���", true);
		
		// ��ư �׷쿡 3���� ������ư ����
		g.add(rb1);
		g.add(rb2);

		// ����Ʈ�ҿ� 3 ���� ������ư ����
		c.add(rb1); c.add(rb2); 

		setSize(250,150);
		setVisible(true);
		
	}
	
	public static void main(String[] args) {
		new JRadioButtonTest();
	}

}
