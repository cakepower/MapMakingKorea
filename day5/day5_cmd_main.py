#!__*__coding:utf-8__*__
import cmd, sys
import day5_final as d
import day5_naver_api_01 as naver

class MyShell(cmd.Cmd):
    intro = """
    ==========================================
    파이쎤 데이터 분석 실무 프로그램입니다. 
    help 나 ?를 눌러서 도움말을 보십시오
    ==========================================
    """
    prompt = '(명령어를 입력해주세요) >> '
    doc_header = "도움말은"
    # ----- basic turtle commands -----
    def do_file(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        #d.csv_file_open3()
    def do_movie(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        #d.get_movie_data()
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
    def do_quit(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('이용해 주셔서 감사합니다.')
        return True

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('이용해 주셔서 감사합니다.')
        return True

    def do_naver_blog(self, arg):
        """
            네이버에서 값을 가지고 옵니다.
        """
        naver.run_naver_search_from_blog(arg)

    def do_naver_news(self, arg):
        """
            네이버에서 값을 가지고 옵니다.
        """
        naver.run_naver_search_from_news(arg)

    def __precmd(self, line):
        line = line.lower()
        print("precmd" + line)
        return line

    def __postcmd(self, stop, line):
        print(stop)
        print("postcmd:" + line)
        return stop

if __name__ == '__main__':
    MyShell().cmdloop()