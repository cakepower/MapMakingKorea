#!__*__coding:utf-8__*__
import cmd, sys
import day32_final as d
import Naver_api as naver

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
        'csv 파일을 입력하여 주십시요'
        d.csv_file_open3()
    def do_movie(self, arg):
        '영화 정보를 가지고 옵니다'
        d.get_movie_data()
    def do_home(self, arg):
        'Home 페이지로 돌아갑니다'
    def do_quit(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('이용해 주셔서 감사합니다.')
        return True
    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('이용해 주셔서 감사합니다.')
        return True

    def do_naver_blog(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        naver.run_naver_search_from_blog(arg)
        print('naver blog 에서 검색하여 %s 결과값을 파일에 저장합니다.' % arg)

    def do_naver_news(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        naver.run_naver_search_from_news(arg)
        print('naver news 에서 검색하여 %s 결과값을 파일에 저장합니다.' % arg)

    def __precmd(self, line):
        line = line.lower()
        print("precmd" + line)
        return line

    def __postcmd(self, stop, line):
        print(stop)
        print("postcmd" + line)
        return stop

if __name__ == '__main__':
    MyShell().cmdloop()