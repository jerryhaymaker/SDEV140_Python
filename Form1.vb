Public Class FinalExam
    Private Sub txtNumInput_TextChanged(sender As Object, e As EventArgs) Handles txtNumInput.TextChanged

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles btnDoubleIntegerInput.Click
        Dim doubleIntegerInput As Integer
        doubleIntegerInput = Convert.ToInt32(txtNumInput.Text)
        doubleIntegerInput = doubleIntegerInput + doubleIntegerInput
        MessageBox.Show(doubleIntegerInput)
        txtNumInput.Text = ""
    End Sub

    Private Sub btnHalfIntegerInput_Click(sender As Object, e As EventArgs) Handles btnHalfIntegerInput.Click
        Dim halfIntegerInput As Double
        halfIntegerInput = Convert.ToInt32(txtNumInput.Text)
        halfIntegerInput = halfIntegerInput / 2
        MessageBox.Show(halfIntegerInput)
        txtNumInput.Text = ""
    End Sub

    Private Sub FinalExam_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class
