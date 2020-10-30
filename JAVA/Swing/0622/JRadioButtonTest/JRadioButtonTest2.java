import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.ButtonGroup;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JRadioButton;

public class JRadioButtonTest2 extends JFrame {
	
	public JRadioButtonTest2() {
		setTitle("������ư �����  ����");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(new FlowLayout());

		ButtonGroup g = new ButtonGroup();  // ��ư �׷� ��ü ����
		
		// ������ư 2�� ����
		JRadioButton rb1 = new JRadioButton("�ڹ�");
		JRadioButton rb2 = new JRadioButton("C���", true);
		
		rb1.addItemListener(listener);
		rb2.addItemListener(listener);
		
		// ��ư �׷쿡 3���� ������ư ����
		g.add(rb1);
		g.add(rb2);

		// ����Ʈ�ҿ� 3 ���� ������ư ����
		c.add(rb1); c.add(rb2); 

		setSize(250,150);
		setVisible(true);
		
	}
	
	public static void main(String[] args) {
		new JRadioButtonTest2();
	}
	
	ItemListener listener = new ItemListener() {
		
		@Override
		public void itemStateChanged(ItemEvent e) {
			
			JRadioButton cb = (JRadioButton)e.getSource();
			String str = cb.getText();
			if(e.getStateChange() == ItemEvent.SELECTED) {
				str = str + "������ ����";
			}
			else {
				str = str + "������ ����";
			}
			
			System.out.println(str);
		}
	};

}
