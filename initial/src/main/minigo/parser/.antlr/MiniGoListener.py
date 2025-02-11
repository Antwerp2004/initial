# Generated from c://Users//HP//Downloads//Principles of Programming Language (CO3005)//Assignment//Assignment 1//initial//initial//src//main//minigo//parser//MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl.
    def enterDecl(self, ctx:MiniGoParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl.
    def exitDecl(self, ctx:MiniGoParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmt.
    def enterStmt(self, ctx:MiniGoParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmt.
    def exitStmt(self, ctx:MiniGoParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#block.
    def enterBlock(self, ctx:MiniGoParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#block.
    def exitBlock(self, ctx:MiniGoParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl.
    def enterVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl.
    def exitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#const_decl.
    def enterConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#const_decl.
    def exitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_stmt.
    def enterAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_stmt.
    def exitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#lhs.
    def enterLhs(self, ctx:MiniGoParser.LhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#lhs.
    def exitLhs(self, ctx:MiniGoParser.LhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_stmt.
    def enterIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_stmt.
    def exitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#only_if_stmt.
    def enterOnly_if_stmt(self, ctx:MiniGoParser.Only_if_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#only_if_stmt.
    def exitOnly_if_stmt(self, ctx:MiniGoParser.Only_if_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_if_list.
    def enterElse_if_list(self, ctx:MiniGoParser.Else_if_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_if_list.
    def exitElse_if_list(self, ctx:MiniGoParser.Else_if_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_stmt.
    def enterElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_stmt.
    def exitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_stmt.
    def enterFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_stmt.
    def exitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#basic_for_loop.
    def enterBasic_for_loop(self, ctx:MiniGoParser.Basic_for_loopContext):
        pass

    # Exit a parse tree produced by MiniGoParser#basic_for_loop.
    def exitBasic_for_loop(self, ctx:MiniGoParser.Basic_for_loopContext):
        pass


    # Enter a parse tree produced by MiniGoParser#condition.
    def enterCondition(self, ctx:MiniGoParser.ConditionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#condition.
    def exitCondition(self, ctx:MiniGoParser.ConditionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_loop_initial.
    def enterFor_loop_initial(self, ctx:MiniGoParser.For_loop_initialContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_loop_initial.
    def exitFor_loop_initial(self, ctx:MiniGoParser.For_loop_initialContext):
        pass


    # Enter a parse tree produced by MiniGoParser#initialization.
    def enterInitialization(self, ctx:MiniGoParser.InitializationContext):
        pass

    # Exit a parse tree produced by MiniGoParser#initialization.
    def exitInitialization(self, ctx:MiniGoParser.InitializationContext):
        pass


    # Enter a parse tree produced by MiniGoParser#update.
    def enterUpdate(self, ctx:MiniGoParser.UpdateContext):
        pass

    # Exit a parse tree produced by MiniGoParser#update.
    def exitUpdate(self, ctx:MiniGoParser.UpdateContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_loop_range.
    def enterFor_loop_range(self, ctx:MiniGoParser.For_loop_rangeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_loop_range.
    def exitFor_loop_range(self, ctx:MiniGoParser.For_loop_rangeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#break_stmt.
    def enterBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#break_stmt.
    def exitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continue_stmt.
    def enterContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continue_stmt.
    def exitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#call_stmt.
    def enterCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#call_stmt.
    def exitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_stmt.
    def enterReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_stmt.
    def exitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_decl.
    def enterFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_decl.
    def exitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_call.
    def enterFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_call.
    def exitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#argument_list.
    def enterArgument_list(self, ctx:MiniGoParser.Argument_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#argument_list.
    def exitArgument_list(self, ctx:MiniGoParser.Argument_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_decl.
    def enterMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_decl.
    def exitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_call.
    def enterMethod_call(self, ctx:MiniGoParser.Method_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_call.
    def exitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primitive_type.
    def enterPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primitive_type.
    def exitPrimitive_type(self, ctx:MiniGoParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typ.
    def enterTyp(self, ctx:MiniGoParser.TypContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typ.
    def exitTyp(self, ctx:MiniGoParser.TypContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr.
    def enterExpr(self, ctx:MiniGoParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expr.
    def exitExpr(self, ctx:MiniGoParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr1.
    def enterExpr1(self, ctx:MiniGoParser.Expr1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr1.
    def exitExpr1(self, ctx:MiniGoParser.Expr1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr2.
    def enterExpr2(self, ctx:MiniGoParser.Expr2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr2.
    def exitExpr2(self, ctx:MiniGoParser.Expr2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr3.
    def enterExpr3(self, ctx:MiniGoParser.Expr3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr3.
    def exitExpr3(self, ctx:MiniGoParser.Expr3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr4.
    def enterExpr4(self, ctx:MiniGoParser.Expr4Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr4.
    def exitExpr4(self, ctx:MiniGoParser.Expr4Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr5.
    def enterExpr5(self, ctx:MiniGoParser.Expr5Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr5.
    def exitExpr5(self, ctx:MiniGoParser.Expr5Context):
        pass


    # Enter a parse tree produced by MiniGoParser#sub_expr.
    def enterSub_expr(self, ctx:MiniGoParser.Sub_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#sub_expr.
    def exitSub_expr(self, ctx:MiniGoParser.Sub_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#operand.
    def enterOperand(self, ctx:MiniGoParser.OperandContext):
        pass

    # Exit a parse tree produced by MiniGoParser#operand.
    def exitOperand(self, ctx:MiniGoParser.OperandContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_decl.
    def enterArray_decl(self, ctx:MiniGoParser.Array_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_decl.
    def exitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_type.
    def enterArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_type.
    def exitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_size_box.
    def enterArray_size_box(self, ctx:MiniGoParser.Array_size_boxContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_size_box.
    def exitArray_size_box(self, ctx:MiniGoParser.Array_size_boxContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_literal.
    def enterArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_literal.
    def exitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_ele_list.
    def enterArray_ele_list(self, ctx:MiniGoParser.Array_ele_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_ele_list.
    def exitArray_ele_list(self, ctx:MiniGoParser.Array_ele_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_ele.
    def enterArray_ele(self, ctx:MiniGoParser.Array_eleContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_ele.
    def exitArray_ele(self, ctx:MiniGoParser.Array_eleContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_access.
    def enterArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_access.
    def exitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_decl.
    def enterStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_decl.
    def exitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_list.
    def enterField_list(self, ctx:MiniGoParser.Field_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_list.
    def exitField_list(self, ctx:MiniGoParser.Field_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_literal.
    def enterStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_literal.
    def exitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_ele_list.
    def enterStruct_ele_list(self, ctx:MiniGoParser.Struct_ele_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_ele_list.
    def exitStruct_ele_list(self, ctx:MiniGoParser.Struct_ele_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_ele.
    def enterStruct_ele(self, ctx:MiniGoParser.Struct_eleContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_ele.
    def exitStruct_ele(self, ctx:MiniGoParser.Struct_eleContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_access.
    def enterStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_access.
    def exitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_decl.
    def enterInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_decl.
    def exitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_method.
    def enterInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_method.
    def exitInterface_method(self, ctx:MiniGoParser.Interface_methodContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param_list.
    def enterParam_list(self, ctx:MiniGoParser.Param_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param_list.
    def exitParam_list(self, ctx:MiniGoParser.Param_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param_decl.
    def enterParam_decl(self, ctx:MiniGoParser.Param_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param_decl.
    def exitParam_decl(self, ctx:MiniGoParser.Param_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arith_high_operator.
    def enterArith_high_operator(self, ctx:MiniGoParser.Arith_high_operatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arith_high_operator.
    def exitArith_high_operator(self, ctx:MiniGoParser.Arith_high_operatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arith_low_operator.
    def enterArith_low_operator(self, ctx:MiniGoParser.Arith_low_operatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arith_low_operator.
    def exitArith_low_operator(self, ctx:MiniGoParser.Arith_low_operatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#relational_operator.
    def enterRelational_operator(self, ctx:MiniGoParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#relational_operator.
    def exitRelational_operator(self, ctx:MiniGoParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_operator.
    def enterAssign_operator(self, ctx:MiniGoParser.Assign_operatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_operator.
    def exitAssign_operator(self, ctx:MiniGoParser.Assign_operatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#comment.
    def enterComment(self, ctx:MiniGoParser.CommentContext):
        pass

    # Exit a parse tree produced by MiniGoParser#comment.
    def exitComment(self, ctx:MiniGoParser.CommentContext):
        pass



del MiniGoParser